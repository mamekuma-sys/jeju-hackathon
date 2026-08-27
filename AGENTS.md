# Universal agent operating instructions

These instructions are vendor-neutral. Apply them whether the current runtime is a coding CLI, IDE agent, hosted agent, terminal agent, or a manually coordinated set of chat sessions.

## Source of truth

1. Read `SPEC.md` and `PLAN.md` before changing code.
2. Treat the 90-second demo path and `Definition of Done` in `SPEC.md` as the acceptance contract.
3. If a requested change conflicts with the spec, state the conflict and update the spec only when the user approves or the request explicitly changes scope.
4. Record meaningful scope, contract, and architecture decisions in `PLAN.md`.

## Priority order

1. A working end-to-end demo path
2. Reliability and recoverable failure states
3. Clear user experience
4. Verification evidence
5. Code quality needed for safe iteration
6. Nice-to-have features

## Working rules

- Inspect the current implementation before editing.
- Make the smallest coherent change that advances a `Must have` acceptance criterion.
- Do not refactor unrelated code, introduce speculative abstractions, or replace working infrastructure during the hackathon.
- Reuse existing components, patterns, dependencies, and scripts when reasonable.
- Never commit secrets. Keep privileged API calls server-side and maintain `.env.example` with placeholder values only.
- Preserve user changes and call out overlapping edits before touching them.
- Prefer a vertical slice that can be demonstrated over disconnected layers that are individually polished.

## Planning and ownership

- Every implementation task must have: one owner, explicit owned paths, dependencies, and an observable done condition in `PLAN.md`.
- At the start of an orchestrated run, identify the available execution mode: native delegation, parallel sessions/worktrees, or sequential fallback.
- Only run work in parallel when the user or an invoked workflow requests it and the work is genuinely independent.
- Parallel write agents or sessions must own disjoint paths. Shared contracts are agreed first; shared configuration, lockfiles, and integration files stay with the coordinator unless explicitly assigned.
- Use isolated read-only contexts for exploration, test analysis, and review when the runtime supports them.
- If the runtime has no subagents, execute the same roles sequentially and start Reviewer in a fresh context when possible.
- The coordinator waits for all assigned work, integrates it, runs repository-wide checks, and owns the final result.

## Portable role contract

- Canonical role definitions live in `.agents/agents/`.
- A product-specific adapter may point to a canonical role but must not redefine its behavior.
- When a named role is unavailable natively, read the matching role file and perform that role directly.
- Do not depend on a product-specific agent name in `SPEC.md`, `PLAN.md`, or acceptance criteria.
- Roles exchange self-contained handoffs: task, changed files, evidence, assumptions, risks, and next action.

## Implementation loop

For each task:

1. Identify the acceptance criterion and affected paths.
2. Inspect existing code and agree on any shared contract.
3. Implement the smallest usable slice.
4. Run the narrowest relevant check.
5. Integrate and run the broader checks from `SPEC.md`.
6. Exercise the real demo path when UI or integration behavior changes.
7. Record exact verification evidence and remaining risks in `PLAN.md`.

On failure, read the actual output, form one concrete hypothesis, make one focused fix, and rerun the failed check. After three unsuccessful attempts on the same issue, stop looping and report the evidence, likely cause, and smallest fallback.

## Verification and completion

- Never claim completion from code inspection alone when the behavior can be executed.
- Use the exact commands listed in `SPEC.md`. If they are stale, discover the correct project commands and update the table.
- For web UI changes, verify the real page when browser tooling is available: primary flow, loading, empty/error state, console errors, obvious responsive breakage, and keyboard focus.
- A check that could not run is `NOT VERIFIED`, never a pass.
- Report completion with: changed files, commands/actions run, pass/fail results, and remaining risks.

## Review severity

- `P0`: breaks the primary demo, loses data, exposes secrets, or creates a serious security issue.
- `P1`: violates a Must-have criterion or makes the main flow unreliable.
- `P2`: meaningful UX, maintainability, accessibility, or edge-case defect that can wait until the vertical slice works.
- `P3`: polish or optional improvement.

During demo freeze, fix only P0/P1 issues unless the user explicitly changes the freeze.

## Demo freeze

When the final 20% of the event begins:

- Do not add features or replace dependencies.
- Fix only demo-blocking defects.
- Run the complete demo three times from a clean start.
- Verify the fallback path in `SPEC.md` and update `DEMO.md`.
- Preserve the last known-good version before risky fixes.
