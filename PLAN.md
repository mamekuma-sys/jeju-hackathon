# Execution Plan

> Planner가 이 파일을 구체화하고, 구현 에이전트가 상태와 검증 증거를 갱신한다. 각 쓰기 작업은 동시에 한 명의 소유자만 가진다.

## Current milestone

- 목표: `[TODO: 첫 번째 end-to-end 수직 슬라이스]`
- 현재 상태: `NOT STARTED`
- 데모 프리즈 시각: `[TODO]`

## Decision log

| 시각 | 결정 | 이유 | 영향 파일 |
| --- | --- | --- | --- |
| `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` |

## Work board

| ID | 우선순위 | 소유자 | 상태 | 의존성 | 소유 경로 | 완료 조건 |
| --- | --- | --- | --- | --- | --- | --- |
| T-01 | P0 | Planner | TODO | - | docs only | SPEC의 TODO와 모순·미결정 목록 정리 |
| T-02 | P0 | Frontend | TODO | T-01 | `[SPEC에서 복사]` | 핵심 화면이 실제 데이터 계약으로 렌더링 |
| T-03 | P0 | Backend | TODO | T-01 | `[SPEC에서 복사]` | 핵심 API/로직과 실패 응답 동작 |
| T-04 | P0 | Integrator | TODO | T-02, T-03 | shared/config only | 90초 경로 end-to-end 성공 |
| T-05 | P0 | Reviewer | TODO | T-04 | read-only | 명령·브라우저·SPEC 검증 보고서 작성 |
| T-06 | P0 | Fix owner | TODO | T-05 | issue-specific | P0/P1 결함 0개 |

상태는 `TODO`, `IN PROGRESS`, `BLOCKED`, `DONE` 중 하나만 사용한다.

## Shared contracts

구현 전에 Frontend와 Backend가 합의해야 하는 최소 계약을 적는다.

```text
[TODO: endpoint/function]
request:
response:
error:
sample:
```

## Verification evidence

| 시각 | 작업 | 명령/동작 | 결과 | 증거 또는 남은 문제 |
| --- | --- | --- | --- | --- |
| `[TODO]` | `[TODO]` | `[TODO]` | PASS/FAIL | `[TODO]` |

## Blockers

- 없음. 문제가 생기면 `문제 / 영향 / 가장 작은 우회책 / 결정권자` 형식으로 적는다.

