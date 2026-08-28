# Agent Compatibility

이 저장소의 핵심은 제품별 설정이 아니라 다음의 공개 Markdown 계약입니다.

```text
AGENTS.md                  공통 프로젝트 규칙
SPEC.md                    제품/완료 계약
PLAN.md                    Coordinator-only 작업/소유권/증거
RUNTIME_CONTRACT.md        입력/도구 결과/승인/재시도 계약
EVALS.md                   실행 구조 실패 평가
.agents/agents/*.md        역할 계약
prompts/*.md               실행 절차
```

도구 전용 파일이 없어도 위 파일을 읽을 수 있는 에이전트라면 전체 워크플로를 실행할 수 있습니다.

## 자동 로딩과 어댑터

| 도구/계열 | 프로젝트 규칙 | 역할 사용 방법 |
| --- | --- | --- |
| AGENTS.md 호환 에이전트 | 루트 `AGENTS.md`를 직접 사용 | `.agents/agents/*.md`를 네이티브 역할 또는 일반 프롬프트로 사용 |
| Claude Code | `CLAUDE.md`가 `AGENTS.md`를 import | `.claude/agents/*.md` 네이티브 어댑터 또는 범용 역할 파일 |
| Gemini CLI | `GEMINI.md`가 `AGENTS.md`를 import | 범용 역할 파일을 읽고 네이티브 agent/세션 기능 또는 순차 모드 사용 |
| Kimi Code | `AGENTS.md` 직접 로딩 | `.agents/agents/*.md`를 프로젝트 custom agent로 자동 발견 |
| Codex | `AGENTS.md` 직접 로딩 | `.codex/agents/*.toml` 네이티브 어댑터 또는 범용 역할 파일 |
| Cursor | `AGENTS.md` 직접 로딩 가능한 표면에서는 그대로 사용 | Agent/Background Agent/독립 세션에 범용 역할 전달 |
| GitHub Copilot | `AGENTS.md` 지원 표면 또는 `.github/copilot-instructions.md` bridge | Copilot agent/custom agent 또는 별도 세션에 범용 역할 전달 |
| Windsurf Cascade | 루트 `AGENTS.md`를 workspace rule로 사용 | Cascade 세션 또는 Worktree별로 범용 역할 전달 |
| Cline, Roo, Aider, OpenCode, Devin 및 기타 | 자동 인식하면 `AGENTS.md`, 아니면 첫 프롬프트에 명시적으로 첨부 | 역할 파일을 새 task/session에 붙여 넣거나 순차 실행 |

이 표는 제품을 지원 범위의 경계로 삼지 않습니다. 새로운 도구도 아래 Capability Check만 통과하면 같은 방식으로 사용할 수 있습니다.

## Capability Check

Kickoff 전에 현재 도구에 다음을 확인합니다. 이 확인은 가장 복잡한 기능을 고르기 위한 것이 아니라, 단일 Coordinator로 부족할 때 사용할 수 있는 안전한 선택지를 파악하기 위한 것입니다.

1. 저장소 파일을 읽고 수정할 수 있는가?
2. shell/test/build/browser 중 무엇을 실행할 수 있는가?
3. 하위 에이전트, agent team, swarm, background task가 있는가?
4. 독립 세션이나 Git Worktree를 만들 수 있는가?
5. 읽기 전용 Reviewer 컨텍스트를 만들 수 있는가?
6. 승인, sandbox, 네트워크, 비밀값 제한은 무엇인가?

기본값은 언제나 단일 Coordinator입니다. 대답과 `AGENTS.md`의 병렬 Gate에 따라 필요한 기능만 추가합니다.

```text
기본                         → 한 Coordinator가 역할을 순차 적용
탐색/리뷰 격리가 필요함       → 읽기 전용 역할 하나만 위임
병렬 Gate를 모두 통과함       → 비중첩 Task packet만 worker/세션/Worktree에 위임
위임 기능이 없음              → 같은 역할 파일을 단일 세션에서 순차 적용
```

## 역할을 수동으로 실행하는 공통 문장

네이티브 agent 파일을 읽지 않는 도구에서는 다음 형식을 사용합니다.

```text
AGENTS.md, SPEC.md, PLAN.md와 .agents/agents/<ROLE>.md를 읽어.
이번 작업에서는 <ROLE> 역할만 수행해.
Task ID: <ID>
Owned paths: <PATHS>
Forbidden paths: <PATHS>
Acceptance criteria: <CRITERIA>
완료 후 역할 파일에 정의된 self-contained handoff만 반환해.
```

## 공급자 전환 규칙

- 모델이나 제품을 바꿔도 `SPEC.md`와 `PLAN.md`를 복사하지 않는다. 같은 파일을 기준으로 삼는다.
- 제품 전용 메모리보다 저장소의 검증 가능한 사실을 우선한다.
- 역할 이름이 달라도 Planner/Builder/Reviewer 계약을 유지한다.
- native delegation이 가능하다는 이유만으로 역할을 분리하지 않는다.
- 네이티브 병렬 기능이 없으면 동작을 생략하지 말고 순차 실행한다.
- 도구가 완료했다고 말해도 실행 증거가 없으면 `NOT VERIFIED`다.
