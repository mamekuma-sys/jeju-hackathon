# Hackathon Operating Loop

## 전체 흐름

```text
DEMO STORY
    ↓
SPEC LOCK
    ↓
PLAN + CONTRACTS
    ↓
PARALLEL BUILD (disjoint paths only)
    ↓
COORDINATOR INTEGRATION
    ↓
RUN + TEST + BROWSER VERIFY
    ↓
REVIEWER FINDINGS
    ↓
P0/P1? ── yes → FOCUSED FIX → VERIFY ─┐
    │                                  │
    no                                 └───────┘
    ↓
DEMO FREEZE → 3 REHEARSALS → SHIP
```

## Phase 0 — 준비 (전체 시간의 0–10%)

1. `SPEC.md`의 TODO를 채운다.
2. 90초 데모 대본을 먼저 적는다.
3. Must have를 최대 3–5개로 자른다.
4. 외부 API가 있다면 fixture/mock fallback을 정한다.
5. 실행·테스트·빌드 명령을 실제로 한 번 실행해 `SPEC.md`에 확정한다.

종료 조건: 팀원이 같은 데모 경로와 `Done`을 말할 수 있다.

## Phase 1 — 계획과 계약 (10–15%)

`prompts/10-plan.md`를 실행한다. 계획 검토 시 다음만 본다.

- 첫 작업이 end-to-end 수직 슬라이스인가?
- Frontend/Backend 소유 경로가 겹치지 않는가?
- API/타입/샘플 응답 계약이 구현 전에 고정됐는가?
- 각 작업의 완료 조건을 실제로 관찰할 수 있는가?
- Nice to have가 임계 경로에 섞이지 않았는가?

종료 조건: `PLAN.md`의 P0 작업, 의존성, 소유 경로가 확정됐다.

## Phase 2 — 병렬 구현 (15–60%)

`prompts/20-build-parallel.md`를 실행한다.

- Frontend와 Backend가 독립적일 때만 동시에 쓴다.
- 공용 타입/스키마를 먼저 확정하고 한 명만 수정한다.
- 루트 설정, lockfile, 배포 설정은 Coordinator가 통합 시 다룬다.
- 각 agent는 자신의 좁은 검증을 실행하고 결과를 반환한다.

15–20분마다 확인할 질문:

1. 지금 데모 경로가 전보다 더 많이 동작하는가?
2. 가장 큰 막힘은 코드인가, 결정인가, 외부 의존성인가?
3. 지금 기능 하나를 버리면 핵심 데모가 더 빨리 완성되는가?

종료 조건: 실제 입력부터 결과까지 첫 수직 슬라이스가 동작한다.

## Phase 3 — 통합과 검증 (60–80%)

Coordinator가 변경을 통합한 뒤 `prompts/30-review-loop.md`를 실행한다.

검증 순서:

1. 설치 및 앱 시작
2. lint/typecheck/unit test
3. production build
4. 핵심 API smoke test
5. 브라우저에서 90초 데모 경로
6. 로딩/오류/빈 상태
7. Reviewer의 SPEC 대조 검사

하나가 실패하면:

```text
actual failure → one hypothesis → smallest fix → rerun failed check
```

같은 실패를 세 번 고치지 못하면 자동 반복을 멈추고 fallback으로 전환할지 결정한다.

종료 조건: P0/P1이 없고, 실행 증거가 `PLAN.md`에 남았다.

## Phase 4 — Demo freeze (마지막 20%)

`prompts/40-demo-freeze.md`를 실행한다.

- 새 기능, 새 의존성, 큰 리팩터링 금지
- 데모를 clean start에서 3회 연속 실행
- API 실패와 배포 실패 fallback 각각 1회 실행
- 발표자가 클릭하는 동안 다른 팀원이 복구 담당
- 마지막 known-good commit/tag를 기록

## 긴급 의사결정 규칙

| 상황 | 기본 결정 |
| --- | --- |
| P0 버그가 30분 이상 지속 | 범위를 줄이거나 fixture fallback 사용 |
| Frontend/Backend 계약 충돌 | Coordinator가 계약을 고정하고 양쪽 수정 순서를 직렬화 |
| 외부 API 불안정 | 캐시된 실제 형식의 응답으로 데모하고 연동 코드는 유지 |
| 배포만 실패 | localhost 데모로 즉시 전환 |
| 시간이 20% 미만 | 새 기능 중단, P0/P1과 대본만 수정 |
| 기능은 많지만 Wow가 약함 | 기능 추가 대신 결과 화면과 설명을 다듬음 |

## 사람의 역할

AI 에이전트가 코드를 쓰는 동안 사람은 다음을 소유한다.

- 문제와 데모 이야기가 설득력 있는지 판단
- 범위 삭제 결정
- 외부 API 키/계정/데이터 준비
- 실제 화면을 보고 맛과 우선순위 판단
- 에이전트의 완료 보고가 아니라 실행 결과 확인
- 마지막 발표와 fallback 전환
