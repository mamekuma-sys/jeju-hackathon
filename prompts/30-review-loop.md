# Independent review and fix prompt

```text
통합된 구현 또는 고영향 산출물을 SPEC.md, QUALITY_REFLEXES.md와 .agents/agents/reviewer.md에 맞춰 검토해.

1. Coordinator가 먼저 lint/typecheck/test/build/smoke, Primary journey와 선언된 Demo contract를 실행하고 PLAN.md에 증거를 기록해.
2. 일반 구현 review에서는 Reviewer를 가능한 한 별도 읽기 전용 컨텍스트로 실행해. Reviewer는 코드나 PLAN.md를 수정하지 않고 제공된 증거의 대상·신선도·의미를 확인해.
3. `QUALITY_REFLEXES.md`의 FRESH_EYES trigger가 발화하면 Reviewer의 artifact-only mode와 그 입력 경계를 그대로 사용해.
4. 같은 문서에 정의된 evaluation artifact가 실질적으로 바뀌었으면 EVAL_INDEPENDENCE를 한 번 실행해.
5. 일반 review finding에는 severity, acceptance criterion, file/symbol 또는 runtime step, reproduction/evidence, smallest remediation을 포함해.
6. Coordinator가 finding을 재현하고 확인된 P0/P1만 최소 수정해.
7. 실패한 좁은 검사부터 전체 검증까지 다시 실행한 뒤 영향받은 review만 다시 적용해.

최대 3 fix cycle까지만 허용해. 이후에는 자동 수정을 멈추고 시도, 실제 출력, 남은 위험, smallest fallback을 제시해. PASS는 P0/P1 0개, 실행 가능한 Primary journey 증거와 선언된 timebox 안의 대표 데모 증거가 있을 때만 가능해.
```
