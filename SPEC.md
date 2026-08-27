# Product Spec

> 이 문서는 제품 범위와 `Done`의 단일 기준점이다. 구현을 시작하기 전에 모든 `TODO`를 채운다. 중요한 방향이 바뀌면 코드보다 이 문서를 먼저 갱신한다.

## 1. One-liner

**우리는 `[TODO: 대상 사용자]`가 `[TODO: 문제]`를 `[TODO: 핵심 방식]`으로 해결하도록 돕는다.**

## 2. Why now

- 사용자 문제: `[TODO]`
- 기존 방식의 한계: `[TODO]`
- 우리만의 차별점: `[TODO]`

## 3. 90초 데모 경로

심사위원에게 실제로 보여줄 한 가지 경로만 적는다.

1. **시작 상태:** `[TODO: 사용자가 보는 첫 화면/초기 데이터]`
2. **사용자 행동:** `[TODO: 입력, 업로드, 클릭 등]`
3. **Wow #1:** `[TODO: 즉시 눈에 보이는 변화]`
4. **핵심 처리:** `[TODO: AI/API/알고리즘이 하는 일]`
5. **Wow #2:** `[TODO: 결과 화면과 가치]`
6. **마무리:** `[TODO: 저장, 공유, 비교 등 선택 사항]`

### 데모 성공 문장

`[TODO: 어떤 입력을 넣으면 어떤 결과가 몇 초 안에 나타난다.]`

## 4. Scope

### Must have

- [ ] `[TODO: 데모 시작에 필요한 기능]`
- [ ] `[TODO: 핵심 처리 기능]`
- [ ] `[TODO: 결과를 보여주는 기능]`
- [ ] 실패 시 사용자가 이해할 수 있는 오류 상태
- [ ] 새 환경에서 재현 가능한 실행 방법

### Nice to have

- [ ] `[TODO]`
- [ ] `[TODO]`

### Explicitly out of scope

- `[TODO: 이번 해커톤에서 만들지 않을 것]`
- 프로덕션 규모의 추상화, 조기 최적화, 불필요한 범용화

## 5. User stories and acceptance criteria

### US-01 — `[TODO: 핵심 사용자 행동]`

- Given `[TODO: 초기 조건]`
- When `[TODO: 행동]`
- Then `[TODO: 화면/API/데이터에서 관찰 가능한 결과]`
- Failure state: `[TODO: 실패 시 기대 동작]`

### US-02 — `[TODO: 두 번째 핵심 행동]`

- Given `[TODO]`
- When `[TODO]`
- Then `[TODO]`
- Failure state: `[TODO]`

## 6. Product and visual direction

- 원하는 인상 3개: `[TODO: 예—신뢰감, 빠름, 놀라움]`
- 피할 인상 3개: `[TODO: 예—대시보드 템플릿, 과한 그라디언트, 복잡함]`
- 레퍼런스: `[TODO: URL 또는 첨부 이미지]`
- 데모 화면 크기: `[TODO: 예—1440×900 Chrome]`
- 접근성 최소 기준: 키보드 포커스, 명확한 레이블, 충분한 대비, 오류 메시지

## 7. Technical decisions

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

## 8. Commands

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

## 9. Definition of Done

- [ ] 90초 데모 경로를 새로고침 후 처음부터 끝까지 3회 연속 수행했다.
- [ ] Must have 항목이 모두 충족됐다.
- [ ] `Commands`의 해당 검증 명령이 통과했다.
- [ ] 로딩, 빈 상태, 오류 상태가 데모 경로에서 깨지지 않는다.
- [ ] API 키와 비밀값이 저장소나 클라이언트 번들에 포함되지 않는다.
- [ ] `README.md`만 보고 새 환경에서 실행할 수 있다.
- [ ] `DEMO.md`에 발표 대본과 실패 시 복구 경로가 있다.

## 10. Fallbacks

| 위험 | 감지 방법 | 데모용 대체 경로 |
| --- | --- | --- |
| 외부 API 지연/실패 | `[TODO]` | `[TODO: 캐시된 응답/fixture/mock]` |
| 네트워크 불안정 | `[TODO]` | `[TODO: 로컬 데이터/녹화본]` |
| 배포 장애 | `[TODO]` | `[TODO: localhost 실행]` |

