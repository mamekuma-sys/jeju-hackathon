#!/usr/bin/env python3
"""Validate the portable hackathon agent kit without third-party packages."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python < 3.11
    tomllib = None


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "README.md",
    "AGENTS.md",
    "SPEC.md",
    "PLAN.md",
    "RUNTIME_CONTRACT.md",
    "EVALS.md",
    "ARCHITECTURE_REVIEW.md",
    "HACKATHON_RUNBOOK.md",
    "DEMO.md",
    "prompts/00-kickoff.md",
    "prompts/10-plan.md",
    "prompts/20-build.md",
    "prompts/30-review-loop.md",
    "prompts/40-demo-freeze.md",
)

ROLE_FILES = {
    "planner": "hackathon-planner",
    "frontend-builder": "frontend-builder",
    "backend-builder": "backend-builder",
    "reviewer": "hackathon-reviewer",
}
ROLE_NAMES = tuple(ROLE_FILES)
AGENT_MARKERS = (
    "Default execution model",
    "Trust and data boundary",
    "Approval and external effects",
    "Retry and failure handling",
    "Verification and completion",
)
SKIP_LINK_PREFIXES = ("http://", "https://", "mailto:", "#", "data:")


class Report:
    def __init__(self) -> None:
        self.failures: list[str] = []
        self.warnings: list[str] = []
        self.passes: list[str] = []

    def fail(self, message: str) -> None:
        self.failures.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def ok(self, message: str) -> None:
        self.passes.append(message)

    def print(self) -> None:
        for message in self.passes:
            print(f"PASS {message}")
        for message in self.warnings:
            print(f"WARN {message}")
        for message in self.failures:
            print(f"FAIL {message}")
        print(
            f"SUMMARY pass={len(self.passes)} "
            f"warn={len(self.warnings)} fail={len(self.failures)}"
        )


def read_text(path: Path, report: Report) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        report.fail(f"cannot read {path.relative_to(ROOT)}: {exc}")
        return ""


def check_required_files(report: Report) -> None:
    missing = [name for name in REQUIRED_FILES if not (ROOT / name).is_file()]
    if missing:
        report.fail("missing required files: " + ", ".join(missing))
    else:
        report.ok(f"required files present ({len(REQUIRED_FILES)})")


def check_canonical_roles(report: Report) -> None:
    role_dir = ROOT / ".agents" / "agents"
    names: list[str] = []
    for role, expected_name in ROLE_FILES.items():
        path = role_dir / f"{role}.md"
        if not path.is_file():
            report.fail(f"missing canonical role: {path.relative_to(ROOT)}")
            continue
        metadata = parse_frontmatter(path, report)
        name = metadata.get("name", "")
        description = metadata.get("description", "")
        if name != expected_name:
            report.fail(
                f"{path.relative_to(ROOT)} name must be {expected_name!r}, got {name!r}"
            )
        if not description:
            report.fail(f"{path.relative_to(ROOT)} has no frontmatter description")
        names.append(name)
    duplicates = sorted({name for name in names if name and names.count(name) > 1})
    if duplicates:
        report.fail("duplicate canonical role names: " + ", ".join(duplicates))
    elif len(names) == len(ROLE_NAMES) and not report.failures:
        report.ok("canonical role frontmatter is valid and unique")


def parse_frontmatter(path: Path, report: Report) -> dict[str, str]:
    text = read_text(path, report)
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        report.fail(f"{path.relative_to(ROOT)} has no YAML frontmatter")
        return {}
    try:
        end = lines.index("---", 1)
    except ValueError:
        report.fail(f"{path.relative_to(ROOT)} has unterminated YAML frontmatter")
        return {}
    metadata: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            report.fail(f"{path.relative_to(ROOT)} invalid frontmatter line: {line!r}")
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip("'\"")
    return metadata


def check_claude_adapters(report: Report) -> None:
    names: list[str] = []
    failures_before = len(report.failures)
    for role, expected_name in ROLE_FILES.items():
        path = ROOT / ".claude" / "agents" / f"{role}.md"
        if not path.is_file():
            report.fail(f"missing Claude adapter: {path.relative_to(ROOT)}")
            continue
        metadata = parse_frontmatter(path, report)
        name = metadata.get("name", "")
        if name != expected_name:
            report.fail(
                f"{path.relative_to(ROOT)} name must be {expected_name!r}, got {name!r}"
            )
        if not metadata.get("description"):
            report.fail(f"{path.relative_to(ROOT)} has no frontmatter description")
        names.append(name)
    duplicates = sorted({name for name in names if name and names.count(name) > 1})
    if duplicates:
        report.fail("duplicate Claude adapter names: " + ", ".join(duplicates))
    elif len(names) == len(ROLE_NAMES) and len(report.failures) == failures_before:
        report.ok("Claude adapter frontmatter is valid and unique")


def check_toml_adapters(report: Report) -> None:
    if tomllib is None:
        report.warn("tomllib unavailable; skipped Codex adapter parsing")
        return
    parsed = 0
    for role in ROLE_NAMES:
        path = ROOT / ".codex" / "agents" / f"{role}.toml"
        if not path.is_file():
            report.fail(f"missing TOML adapter: {path.relative_to(ROOT)}")
            continue
        try:
            with path.open("rb") as handle:
                data = tomllib.load(handle)
        except (OSError, tomllib.TOMLDecodeError) as exc:
            report.fail(f"invalid TOML {path.relative_to(ROOT)}: {exc}")
            continue
        if not data:
            report.fail(f"empty TOML adapter: {path.relative_to(ROOT)}")
            continue
        parsed += 1
    config = ROOT / ".codex" / "config.toml"
    try:
        with config.open("rb") as handle:
            tomllib.load(handle)
    except (OSError, tomllib.TOMLDecodeError) as exc:
        report.fail(f"invalid TOML {config.relative_to(ROOT)}: {exc}")
    else:
        parsed += 1
    if parsed == len(ROLE_NAMES) + 1:
        report.ok(f"Codex TOML files parse ({parsed})")


def check_agent_contract(report: Report) -> None:
    text = read_text(ROOT / "AGENTS.md", report)
    missing = [marker for marker in AGENT_MARKERS if marker not in text]
    if missing:
        report.fail("AGENTS.md missing contract sections: " + ", ".join(missing))
    else:
        report.ok("AGENTS.md contains trust, approval, retry, and verification contracts")


def check_prompt_migration(report: Report) -> None:
    old = ROOT / "prompts" / "20-build-parallel.md"
    new = ROOT / "prompts" / "20-build.md"
    if old.exists():
        report.fail("obsolete parallel-first prompt still exists: prompts/20-build-parallel.md")
    elif new.is_file():
        report.ok("single-coordinator build prompt replaced parallel-first prompt")


def check_local_links(report: Report) -> None:
    link_pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
    broken: list[str] = []
    checked = 0
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = read_text(path, report)
        for raw_target in link_pattern.findall(text):
            target = raw_target.strip().split("#", 1)[0].strip()
            target = target.strip("<>")
            if not target or target.startswith(SKIP_LINK_PREFIXES):
                continue
            target = target.split(" ", 1)[0]
            linked = (path.parent / target).resolve()
            checked += 1
            try:
                linked.relative_to(ROOT)
            except ValueError:
                broken.append(f"{path.relative_to(ROOT)} -> {raw_target}")
                continue
            if not linked.exists():
                broken.append(f"{path.relative_to(ROOT)} -> {raw_target}")
    if broken:
        report.fail("broken local Markdown links: " + "; ".join(broken))
    else:
        report.ok(f"local Markdown links resolve ({checked} checked)")


def check_placeholders(report: Report, strict: bool) -> None:
    spec = read_text(ROOT / "SPEC.md", report)
    todo_count = len(re.findall(r"\[TODO(?::[^\]]*)?\]", spec, flags=re.IGNORECASE))
    command_section = spec.split("## 8. Commands", 1)[-1].split("## 9.", 1)[0]
    command_todos = len(re.findall(r"\[TODO(?::[^\]]*)?\]", command_section, flags=re.IGNORECASE))
    if todo_count == 0 and command_todos == 0:
        report.ok("SPEC.md has no unresolved TODO placeholders")
        return
    message = f"SPEC.md unresolved placeholders={todo_count}, command placeholders={command_todos}"
    if strict:
        report.fail(message)
    else:
        report.warn(message + "; use --strict before implementation/demo freeze")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="fail when SPEC.md still contains TODO or command placeholders",
    )
    args = parser.parse_args()
    report = Report()
    check_required_files(report)
    check_canonical_roles(report)
    check_claude_adapters(report)
    check_toml_adapters(report)
    check_agent_contract(report)
    check_prompt_migration(report)
    check_local_links(report)
    check_placeholders(report, args.strict)
    report.print()
    return 1 if report.failures else 0


if __name__ == "__main__":
    sys.exit(main())
