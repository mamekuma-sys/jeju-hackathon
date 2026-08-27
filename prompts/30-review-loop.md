# Independent reviewer + fix loop prompt

```text
통합된 현재 구현을 SPEC.md의 90초 데모와 Definition of Done에 맞춰 검증해줘. Reviewer 역할 계약은 .agents/agents/reviewer.md에 있다.

1. 먼저 Coordinator로 SPEC.md에 적힌 lint/typecheck/test/build/smoke 명령을 실제 실행하고 브라우저 사용이 가능하면 데모 경로를 직접 수행해. 결과를 PLAN.md에 기록해.
2. 가능한 가장 독립적인 Reviewer 컨텍스트를 사용해:
   - 네이티브 하위 에이전트가 있으면 읽기 전용 Reviewer를 호출해.
   - 없으면 별도 세션/다른 에이전트 도구/새 컨텍스트에 reviewer.md와 현재 diff·실행 증거를 전달해.
   - 둘 다 불가능하면 현재 에이전트가 구현 의도를 잠시 배제하고 reviewer.md 체크리스트를 엄격히 적용해.
3. Reviewer 결과를 기다리고 각 finding을 실제 코드와 재현 결과로 확인해. 근거 없는 finding은 기각 사유를 기록해.
4. 확인된 P0/P1만 우선순위대로 가장 작은 수정으로 해결하고, 실패한 좁은 검사부터 전체 검증까지 다시 실행해.
5. 수정 후 독립 Reviewer를 한 번 더 실행해 회귀를 확인해.

최대 3번의 fix cycle까지만 반복해. 이후에도 같은 문제가 남으면 자동 수정을 멈추고 문제, 시도, 실제 출력, 가장 작은 fallback을 제시해. 종료 조건은 P0/P1 0개, 핵심 데모의 실행 증거, PLAN.md 갱신이야.
```

