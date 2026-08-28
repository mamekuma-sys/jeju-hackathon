# Execution Plan and Run State

> `PLAN.md` is the single durable run state. Only the Coordinator edits it. Planner, Builder, and Reviewer roles return handoffs for the Coordinator to apply.

## Run

- Run ID: `[TODO: YYYYMMDD-HHMM-short-name]`
- 목표: `[TODO: 첫 번째 end-to-end 수직 슬라이스]`
- 실행 모드: `SINGLE_COORDINATOR`
- 현재 상태: `NOT STARTED`
- Coordinator: `[TODO]`
- 데모 프리즈 시각: `[TODO]`
- 남은 시간: `[TODO]`

Allowed run states: `NOT STARTED`, `IN PROGRESS`, `VERIFYING`, `BLOCKED`, `DONE`, `FAILED`, `DROPPED`.

## Assumptions and decisions

| 시각 | 종류 | 결정 또는 가정 | 근거 | 다시 확인할 조건 |
| --- | --- | --- | --- | --- |
| `[TODO]` | assumption/decision | `[TODO]` | `[TODO]` | `[TODO]` |

## Work board

| ID | 우선순위 | 소유자 | 상태 | 시도 | 의존성 | 소유 경로 | 금지 경로 | 관찰 가능한 완료 조건 |
| --- | --- | --- | --- | ---: | --- | --- | --- | --- |
| T-01 | P0 | Coordinator | TODO | 0 | - | `SPEC.md`, `PLAN.md` | application code | SPEC의 Blocker TODO와 실행 명령 확정 |
| T-02 | P0 | Coordinator | TODO | 0 | T-01 | `[SPEC에서 복사]` | unrelated/shared paths | 가장 작은 수직 슬라이스가 로컬에서 동작 |
| T-03 | P0 | Optional Worker | TODO | 0 | frozen contract | `[독립 경로가 있을 때만]` | shared/config/lockfile | 할당된 독립 작업과 좁은 검증 완료 |
| T-04 | P0 | Coordinator | TODO | 0 | T-02, T-03 | shared/config/integration | - | 90초 경로 end-to-end 성공 |
| T-05 | P0 | Reviewer | TODO | 0 | T-04 evidence | read-only | all writes | P0/P1 근거 기반 보고서 반환 |
| T-06 | P0 | Coordinator | TODO | 0 | T-05 | issue-specific | unrelated paths | 확인된 P0/P1 0개와 회귀 검증 |

Allowed task states: `TODO`, `IN PROGRESS`, `VERIFYING`, `BLOCKED`, `DONE`, `FAILED`, `DROPPED`.

## Shared contracts

```text
name:
owner:
request:
response:
error:
sample:
version/change rule:
```

## Verification evidence

| 시각 | Task ID | 명령/동작 | 결과 | 대상/버전 | 증거 | 남은 위험 |
| --- | --- | --- | --- | --- | --- | --- |
| `[TODO]` | `[TODO]` | `[TODO]` | PASS/FAIL/NOT VERIFIED | `[TODO]` | `[TODO]` | `[TODO]` |

## Failure log

| 시각 | Task ID | 도구/단계 | 시도 | 분류 | 실제 오류/증거 | 다음 행동 |
| --- | --- | --- | ---: | --- | --- | --- |
| `[TODO]` | `[TODO]` | `[TODO]` | 1 | TRANSIENT/DETERMINISTIC/INVALID_RESULT/PERMISSION/UNKNOWN | `[TODO]` | `[TODO]` |

## External effect ledger

Push, deploy, publish, message, payment, destructive operation, account/permission change를 실행하기 전에 기록한다.

| 시각 | Task ID / idempotency key | 행동 | 정확한 대상 | 승인 근거 | 사전 상태 | 결과/원격 증거 |
| --- | --- | --- | --- | --- | --- | --- |
| `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` |

## Blockers and handoff

Blocker는 다음 형식만 사용한다.

```text
problem:
impact:
evidence:
attempts:
smallest fallback:
decision or approval needed:
```
