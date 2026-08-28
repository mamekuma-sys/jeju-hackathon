# Representative Demo and Rehearsal

> 제품의 전체 사용자 경험은 `SPEC.md`의 Experience contract가 소유한다. 이 문서는 그 경험에서 선언된 Demo timebox 안에 실제로 보여줄 대표 시나리오, demo data와 복구 절차만 소유한다.

## Demo contract summary

- Demo timebox: `[TODO: 행사에서 허용된 실제 시연 시간]`
- Audience: `[TODO]`
- Core proof: `[TODO: 관객이 직접 확인해야 할 제품 가치]`
- Starting state: `[TODO]`
- Live actions: `[TODO]`
- Ending state: `[TODO]`

## Live and seeded state

| 구분 | 내용 | 출처 | 관객에게 표시하는 방법 | Reset 방법 |
| --- | --- | --- | --- | --- |
| Live input/action | `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` |
| Seeded demo state | `[TODO 또는 N/A]` | `[TODO 또는 N/A]` | `[TODO 또는 N/A]` | `[TODO 또는 N/A]` |
| Fixture/mock/cache | `[TODO 또는 N/A]` | `[TODO 또는 N/A]` | `[TODO 또는 N/A]` | `[TODO 또는 N/A]` |

seeded 상태가 장기간 사용, 여러 사용자 또는 누적 데이터를 대신한다면 실제 데이터처럼 암시하지 않는다. 발표 중 새로 수행하는 live action과 미리 준비한 상태를 명확히 구분한다.

## Setup checklist

- [ ] Stable build/commit recorded: `[TODO]`
- [ ] Runtime and environment recorded: `[TODO]`
- [ ] App URL: `[TODO]`
- [ ] Demo account, permissions and data ready: `[TODO]`
- [ ] Seeded/live/fixture labels checked
- [ ] Browser notifications and unrelated tabs closed
- [ ] Zoom/font size and screen resolution checked
- [ ] External API fallback tested
- [ ] Localhost fallback ready
- [ ] Backup video or screenshots ready

## Script

각 행의 목표 시간을 합치면 `Demo timebox` 안에 들어와야 한다. 제품의 전체 Primary journey를 억지로 압축하지 말고, `SPEC.md`의 Core proof를 가장 설득력 있게 보여주는 live action을 선택한다.

| 단계 | 목표 시간 | 화면/행동 | 말할 내용 | 성공 신호 |
| --- | --- | --- | --- | --- |
| Context | `[TODO]` | `[문제와 시작 상태]` | `[누가 어떤 문제를 겪는지]` | 맥락과 초기 상태가 이해됨 |
| Live action | `[TODO]` | `[입력/업로드/선택/편집]` | `[기존 방식과 다른 점]` | 핵심 입력 완료 |
| Processing | `[TODO]` | `[AI/API/알고리즘 처리]` | `[왜 의미 있는지]` | 적절한 feedback 뒤 결과 표시 |
| Result | `[TODO]` | `[결과/Wow]` | `[사용자에게 생기는 가치]` | Core proof가 화면에서 확인됨 |
| Close | `[TODO]` | `[저장/공유/누적 변화/다음 행동]` | `[왜 다시 사용할지]` | 명확한 끝 상태 |

## Full-experience coverage

대표 데모에서 생략한 전체 UX를 숨기지 않는다. 적용되는 여정과 검증 위치를 기록한다.

| Experience contract 항목 | 대표 데모에 포함 | 별도 검증 evidence |
| --- | --- | --- |
| Primary user journey | YES/PARTIAL | `[TODO]` |
| First-use / empty | YES/NO/N/A | `[TODO 또는 N/A]` |
| Secondary journey | YES/NO/N/A | `[TODO 또는 N/A]` |
| Other-actor journey | YES/NO/N/A | `[TODO 또는 N/A]` |
| Return / accumulated value | YES/NO/N/A | `[TODO 또는 N/A]` |

## Recovery lines

- API가 느릴 때: `[TODO: cache/fixture 전환 문장과 동작]`
- 네트워크가 끊길 때: `[TODO]`
- 배포가 깨질 때: `[TODO: localhost URL과 시작 명령]`
- 결과가 예상과 다를 때: `[TODO: 저장된 예시로 이동]`
- seeded/live 상태가 섞였을 때: `[TODO: reset과 구분 설명 또는 N/A]`

## Rehearsal log

| 회차 | 시작 방식 | 대상 commit/environment | 결과 | 실제 시간 | Evidence | 수정할 점 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | clean start | `[TODO]` | TODO | - | - | - |
| 2 | clean start | `[TODO]` | TODO | - | - | - |
| 3 | clean start | `[TODO]` | TODO | - | - | - |
