# Product Spec

> 이 문서는 제품 범위와 `Done`의 단일 기준점이다. 구현을 시작하기 전에 모든 `TODO`를 실제 값 또는 `N/A`로 바꾼다. 중요한 방향이 바뀌면 코드보다 이 문서를 먼저 갱신한다.

## 1. One-liner

**우리는 `[TODO: 대상 사용자]`가 `[TODO: 문제]`를 `[TODO: 핵심 방식]`으로 해결하도록 돕는다.**

## 2. Why now

- 사용자 문제: `[TODO]`
- 기존 방식의 한계: `[TODO]`
- 우리만의 차별점: `[TODO]`

## 3. Experience contract

제품을 실제로 사용하는 전체 경험을 정의한다. 발표 시간에 맞추기 위해 이 여정을 생략하거나 축소하지 않는다.

### Primary user journey

- 사용자 목표: `[TODO: 사용자가 최종적으로 얻으려는 가치]`
- 시작 상태: `[TODO: 첫 화면, 권한, 초기 데이터]`
- 핵심 행동: `[TODO: 입력, 생성, 탐색, 편집 등]`
- 처리와 피드백: `[TODO: loading/progress와 시스템 반응]`
- 성공 결과: `[TODO: 화면/API/데이터에서 관찰 가능한 결과]`
- 완료 후 다음 행동: `[TODO: 저장, 공유, 재방문 등 또는 N/A]`

### Supporting journeys

해당하지 않는 행은 `N/A`로 쓴다.

| 여정 | 대상 | 시작 → 행동 → 결과 | 필요한 이유 |
| --- | --- | --- | --- |
| First-use / empty | `[TODO]` | `[TODO]` | `[TODO]` |
| Secondary | `[TODO 또는 N/A]` | `[TODO 또는 N/A]` | `[TODO 또는 N/A]` |
| Other actor | `[TODO 또는 N/A]` | `[TODO 또는 N/A]` | `[TODO 또는 N/A]` |
| Return visit | `[TODO 또는 N/A]` | `[TODO 또는 N/A]` | `[TODO 또는 N/A]` |

### Required UX states

- Loading/progress: `[TODO]`
- Empty/first-use: `[TODO]`
- Success: `[TODO]`
- Understandable error and recovery: `[TODO]`
- Permission/offline/conflict state: `[TODO 또는 N/A]`

## 4. Demo contract

전체 사용자 경험에서 심사위원이나 이해관계자에게 실제로 보여줄 대표 시나리오를 정의한다. 시간은 고정값이 아니라 행사 규정과 발표 구성에 맞춰 선언한다.

- Demo timebox: `[TODO: 행사에서 허용된 실제 시연 시간]`
- Audience: `[TODO: 심사위원, 고객, 내부 팀 등]`
- Starting state: `[TODO: 빈 상태 또는 준비된 데이터가 있는 상태]`
- Live actions: `[TODO: 발표 중 실제로 수행할 행동]`
- Core proof: `[TODO: 이 시연이 제품 가치를 증명하는 관찰 가능한 사실]`
- Wow moment #1: `[TODO]`
- Wow moment #2: `[TODO 또는 N/A]`
- Ending state: `[TODO: 마지막에 남겨 둘 화면과 메시지]`
- Seeded state disclosure: `[TODO: 미리 준비한 데이터와 현장에서 생성한 데이터의 구분 또는 N/A]`

### Representative demo path

| 단계 | 목표 시간 | 화면/행동 | 성공 신호 |
| --- | --- | --- | --- |
| Context | `[TODO]` | `[TODO: 사용자와 문제를 이해시키는 시작]` | `[TODO]` |
| Live action | `[TODO]` | `[TODO: 핵심 입력/업로드/선택]` | `[TODO]` |
| Processing | `[TODO]` | `[TODO: 시스템 처리와 적절한 피드백]` | `[TODO]` |
| Result | `[TODO]` | `[TODO: 핵심 결과와 사용자 가치]` | `[TODO]` |
| Close | `[TODO]` | `[TODO: 저장/공유/비교/다음 가치]` | `[TODO]` |

### Demo success sentence

`[TODO: 어떤 시작 상태에서 어떤 live action을 하면 어떤 결과가 선언된 timebox 안에 나타난다.]`

## 5. Accumulated-value contract

시간, 반복 사용, 여러 사용자 또는 데이터 누적에 따라 가치가 커지는 제품을 위한 계약이다. 일회성 제품이면 `Applies: NO`로 두고 나머지를 `N/A`로 쓴다.

- Applies: `[TODO: YES 또는 NO]`
- Value horizon: `[TODO: 한 세션, 하루, 한 달, 여러 사용자 등 또는 N/A]`
- First-use state: `[TODO 또는 N/A]`
- Seeded demo state: `[TODO: 누적 상태를 보여줄 정직하게 표기된 demo data 또는 N/A]`
- New live action: `[TODO: 기존 누적 상태에 발표 중 추가할 실제 행동 또는 N/A]`
- Observable before/after: `[TODO: 새 행동이 누적 가치에 미치는 변화 또는 N/A]`
- Return value: `[TODO: 나중에 돌아왔을 때 얻는 가치 또는 N/A]`
- Data provenance/disclosure: `[TODO: seed, fixture, mock, 실제 데이터의 출처와 표시 방법 또는 N/A]`

## 6. Scope

### Must have

- [ ] `[TODO: Primary journey 시작에 필요한 기능]`
- [ ] `[TODO: 핵심 처리 기능]`
- [ ] `[TODO: 사용자가 결과를 이해하고 행동할 수 있는 기능]`
- [ ] 주요 loading, empty, success, error 상태
- [ ] 새 환경에서 재현 가능한 실행 방법

### Nice to have

- [ ] `[TODO]`
- [ ] `[TODO]`

### Explicitly out of scope

- `[TODO: 이번 해커톤에서 만들지 않을 것]`
- 프로덕션 규모의 추상화, 조기 최적화, 불필요한 범용화

## 7. User stories and acceptance criteria

### US-01 — Primary journey

- Given `[TODO: 초기 조건]`
- When `[TODO: 핵심 행동]`
- Then `[TODO: 화면/API/데이터에서 관찰 가능한 결과]`
- Failure state: `[TODO: 실패 시 기대 동작과 recovery]`

### US-02 — Supporting or return journey

- Applies: `[TODO: YES 또는 NO]`
- Given `[TODO 또는 N/A]`
- When `[TODO 또는 N/A]`
- Then `[TODO 또는 N/A]`
- Failure state: `[TODO 또는 N/A]`

### US-03 — Other-actor journey

- Applies: `[TODO: YES 또는 NO]`
- Given `[TODO 또는 N/A]`
- When `[TODO 또는 N/A]`
- Then `[TODO 또는 N/A]`
- Failure state: `[TODO 또는 N/A]`

## 8. Product and visual direction

- 원하는 인상 3개: `[TODO: 예—신뢰감, 빠름, 놀라움]`
- 피할 인상 3개: `[TODO: 예—대시보드 템플릿, 과한 그라디언트, 복잡함]`
- 레퍼런스: `[TODO: URL 또는 첨부 이미지]`
- 주요 사용 화면/기기: `[TODO: 예—모바일 웹, 1440×900 Chrome]`
- 접근성 최소 기준: 키보드 포커스, 명확한 레이블, 충분한 대비, 오류 메시지

## 9. Technical decisions

- Frontend: `[TODO]`
- Backend: `[TODO 또는 없음]`
- Data store: `[TODO 또는 없음]`
- AI/API integrations: `[TODO 또는 없음]`
- Deployment target: `[TODO]`
- Authentication: `[TODO 또는 데모에서는 제외]`

### Ownership boundaries

- Frontend-owned paths: `[TODO: 예—app/, components/, styles/]`
- Backend-owned paths: `[TODO: 예—api/, server/, db/]`
- Shared contracts: `[TODO: 예—types/, schemas/, openapi/]`
- Integration-only files: `[TODO: 예—package.json, lockfile, root config]`

## 10. Commands

에이전트가 추측하지 않도록 실제 명령으로 바꾼다. 해당 없으면 `N/A`로 쓴다.

| 목적 | 명령 |
| --- | --- |
| Install | `[TODO]` |
| Dev | `[TODO]` |
| Lint | `[TODO]` |
| Typecheck | `[TODO]` |
| Unit tests | `[TODO]` |
| Build | `[TODO]` |
| E2E / smoke | `[TODO]` |

## 11. Definition of Done

### Product Done

- [ ] Primary user journey를 실제 시작 상태부터 성공 결과까지 수행했다.
- [ ] 적용되는 supporting, other-actor, return journey의 acceptance를 검증했다.
- [ ] Must have 항목이 모두 충족됐다.
- [ ] `Commands`의 해당 검증 명령이 통과했다.
- [ ] loading, empty, success, error와 적용되는 permission/offline/conflict 상태가 깨지지 않는다.
- [ ] API 키와 비밀값이 저장소나 클라이언트 번들에 포함되지 않는다.
- [ ] 이 제품의 실행 문서만 보고 새 환경에서 실행할 수 있다.

### Demo Ready

- [ ] Representative demo path가 선언된 Demo timebox 안에 끝난다.
- [ ] clean start에서 대표 데모를 처음부터 끝까지 3회 연속 수행했다.
- [ ] seeded, fixture, mock과 live data가 발표자와 관객에게 정직하게 구분된다.
- [ ] 외부 API와 배포 실패 fallback을 각각 검증했다.
- [ ] [`DEMO.md`](DEMO.md)에 발표 대본, 실제 시간, demo data와 복구 경로가 있다.
- [ ] 마지막 known-good commit과 실행 환경을 기록했다.

## 12. Fallbacks

| 위험 | 감지 방법 | 제품 동작 | 대표 데모용 대체 경로 |
| --- | --- | --- | --- |
| 외부 API 지연/실패 | `[TODO]` | `[TODO]` | `[TODO: 같은 contract의 cache/fixture/mock]` |
| 네트워크 불안정 | `[TODO]` | `[TODO]` | `[TODO: 로컬 데이터/녹화본]` |
| 배포 장애 | `[TODO]` | `[TODO]` | `[TODO: localhost 실행]` |
| seeded/live 상태 혼동 | `[TODO 또는 N/A]` | `[TODO 또는 N/A]` | `[TODO: 명확한 label과 reset 방법 또는 N/A]` |
