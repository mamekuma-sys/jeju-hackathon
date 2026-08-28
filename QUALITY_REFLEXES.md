# Conditional Quality Reflexes

이 문서는 산출물 품질을 높이기 위한 조건부 반사의 단일 기준점이다. 반사는 일반 실행 루프를 대체하지 않으며, 실제 trigger가 확인될 때만 필요한 항목을 읽고 적용한다. 정상적인 구현 작업은 추가 모델 리뷰 호출을 0회 수행한다.

## 공통 라우팅 규칙

- 스키마, 타입 검사, 테스트, 빌드, 브라우저 확인, 원문 대조 같은 결정적 검증을 먼저 실행한다.
- 각 반사는 수정 전에 최대 한 번만 호출한다. 수정 뒤에는 그 수정의 영향을 받은 반사 또는 결정적 검사만 한 번 다시 실행한다.
- build 중 반사 finding으로 인한 수정 cycle은 최대 한 번이다. `prompts/30-review-loop.md`의 확인된 P0/P1 수정 cycle은 기존 최대 3회를 유지한다.
- 근거가 없는 finding은 조언이며 acceptance 실패가 아니다. 반사 결과만으로 `PASS`, `DONE`, 또는 외부 사실을 선언하지 않는다.
- 반사는 push, deploy, publish, 메시지 발송, 결제, 계정 변경 같은 외부 효과를 실행하거나 승인할 수 없다.
- 사용자가 호출한 `ADVERSARIAL_DECISION`은 다른 사용자 호출형 반사를 자동으로 시작하지 않는다.
- 여러 반사가 적용될 수 있으면 현재 실패 위험을 가장 직접적으로 줄이는 최소 집합만 고른다. 전체 반사 세트를 관성적으로 로드하거나 순회하지 않는다.

## 라우팅 표

| 반사 | Trigger | Skip condition | 최대 호출 | Owner | Output | 필요한 evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `INTENT_CHECK` | 요청이 길거나 묶여 있음, 범위·지시 대상이 실제로 모호함, 비용·위험·비가역성이 큼, 또는 문맥 확인 뒤에도 결과가 달라지는 해석 두 개가 남음 | 대화·SPEC·PLAN·파일·관례가 한 해석으로 결정하거나 차이가 결과에 중요하지 않음 | 수정/실행 전 1회 | Coordinator | silent pass 또는 단일 surviving fork 형식 | 대조한 문맥과 두 해석이 만드는 실제 결과 차이 |
| `CLEAN_V0` | prompt, spec, plan, runbook 등 내구 산출물에 patch 누적, 규칙 중복, stale delta, 모순된 이력이 있음 | 산출물이 이미 깨끗하거나 대상이 단순히 리팩터링 가능한 application code임 | 수정 전 1회, 영향받은 결과 재검 1회 | Coordinator | `CHANGED` 또는 `UNCHANGED`와 보존·제거 내역 | 전체 산출물과 canonical source의 before/after diff |
| `FRESH_EYES` | 중요한 handoff, demo freeze, release/publication, 고영향 산출물 acceptance 직전 | routine 작업이거나 결정적 검사만으로 acceptance가 충분히 입증됨 | 수정 전 1회, 영향받은 결과 재검 1회 | read-only Reviewer; 수정 결정은 Coordinator | artifact-only 판정 형식 | reviewer에게 전달한 네 입력과 artifact 자체에서 인용 가능한 결함 |
| `EVAL_INDEPENDENCE` | `EVALS.md`, benchmark, score, metric, experiment, grader, success criterion을 만들거나 실질적으로 변경함 | 평가 의미·oracle·fixture·grader가 변하지 않은 문구/서식 수정뿐임 | 수정 전 1회, 영향받은 평가 재검 1회 | Coordinator 또는 read-only Reviewer | 실제로 발화한 leakage pattern과 최소 independence fix만 | 평가 구성요소, ground truth 출처, fixture/grader/target 연결 |
| `ADVERSARIAL_DECISION` | 사용자가 호출했거나 architecture, security, privacy, cost, irreversible, demo-critical 결정임 | routine·가역 결정, 결정적 증거가 이미 결론을 강제함, 또는 구별되는 실패 모드가 2개 미만임 | 결정 전 1회, 영향받은 결정 재검 1회 | Coordinator가 decision owner를 명시 | lens verdict와 불일치 해소 형식 | lens별로 서로 다른 실패 모드와 load-bearing evidence |

## `INTENT_CHECK`

의도 오독에 큰 비용을 쓰기 전에만 실행한다.

1. 원하는 결과를 사용자 문장의 반복이 아닌 다른 말로 내부 요약한다.
2. 대화, `SPEC.md`, `PLAN.md`, 관련 파일과 저장소 관례를 대조한다.
3. 문맥이 해석을 결정하면 질문 없이 진행한다.
4. 결과를 실질적으로 바꾸는 해석이 둘 이상 남으면 가장 영향이 큰 fork 하나만 표면화한다.
5. 작업이 크다는 이유만으로 확인 질문을 만들지 않는다.

표면화할 때만 다음 형식을 사용한다.

```yaml
understood_as:
surviving_fork:
recommended_default:
question:
```

## `CLEAN_V0`

누적된 내구 산출물을 현재의 깨끗한 한 버전으로 되돌릴 때만 실행한다.

1. 대상 전체와 해당 사실의 canonical source를 끝까지 읽는다.
2. 내구성 있는 사실, 유용한 문체, 계약, 검증 evidence를 보존한다.
3. patch history, 중복, stale assumption, process residue를 제거한다.
4. 새 보충 섹션을 붙이기보다 기존 섹션을 현재 사실로 고친다.
5. 실제 개선이 없으면 diff를 만들지 않는다.

application code에는 “정리할 수 있다”는 이유만으로 자동 적용하지 않는다.

```yaml
status: CHANGED|UNCHANGED
durable_truth_preserved:
noise_removed:
evidence:
```

## `FRESH_EYES`

기존 read-only Reviewer를 artifact-only mode로 사용한다. 새 agent나 mutation 권한을 추가하지 않는다. Reviewer에게는 다음 네 입력만 전달한다.

- artifact
- declared audience
- intended outcome
- acceptance criteria

authoring conversation이나 rationale은 acceptance criterion이 직접 요구할 때만 전달한다. Reviewer는 진단만 하고 Coordinator가 수정 여부를 결정한다.

```yaml
verdict: PASS|FAIL|UNCLEAR
missing_context:
misread_risk:
load_bearing_issue:
smallest_fix:
```

## `EVAL_INDEPENDENCE`

평가가 설계자와 grader의 자기확인이 아닌지 읽기 전용으로 감사한다. 다음 중 실제로 확인된 pattern만 반환한다.

- independent ground truth가 평가에 들어오지 않음
- 같은 model 또는 주체가 선호 출력을 설계하고 채점함
- grader가 prompt를 사실상 다시 말할 뿐 외부 동작을 확인하지 않음
- fixture가 기대 답을 드러내는 clue를 포함함
- agent 설명을 외부 behavior 대신 성공으로 측정함
- stale output 또는 잘못된 target도 통과할 수 있음
- evaluator들이 같은 숨은 가정을 공유해 agreement가 circular함

```yaml
- leakage_pattern:
  evidence:
  smallest_independence_fix:
```

아무 pattern도 발화하지 않으면 빈 목록을 반환하며, 그 자체를 평가 정확성의 증명으로 확대하지 않는다.

## `ADVERSARIAL_DECISION`

사용자 호출 또는 고영향 결정에만 적용한다. 실제로 다른 실패 모드를 보는 lens 2–5개를 고르며 같은 reviewer의 이름만 바꾼 복제는 금지한다.

각 lens는 하나의 load-bearing reason만 반환한다.

```yaml
lens:
verdict: PASS|FAIL|UNCLEAR
load_bearing_reason:
```

Coordinator는 lens를 평균내거나 타협 판정으로 뭉개지 않고 다음을 반환한다.

```yaml
agreement:
disagreement:
single_resolving_question:
cheapest_experiment:
decision_owner:
```

## 출처와 채택 범위

이 다섯 반사는 [Paperthin](https://github.com/LilMGenius/paperthin)의 `readchk`, `re0`, `shower`, `mandela`, `prism`, `hate` 메커니즘을 이 저장소의 용어와 실행 계약에 맞게 선택적으로 재정의했다. Paperthin은 LilMGenius의 MIT License로 공개되어 있다. 전체 skill text나 catalog는 복사·설치하지 않았다.

`sip`의 모든 산출물 대상 자동 검사 chain은 routine latency 때문에 채택하지 않았다. `ssotize`와 `detool`은 각각 이 문서의 단일 기준점과 중립 용어 설계에 참고했지만 별도 runtime reflex로 추가하지 않았다.
