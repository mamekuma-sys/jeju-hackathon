# Reviewer + fix loop prompt

```text
통합된 현재 구현을 SPEC.md의 90초 데모와 Definition of Done에 맞춰 검증해줘.

1. 먼저 primary agent로 SPEC.md에 적힌 lint/typecheck/test/build/smoke 명령을 실제 실행하고 브라우저 사용이 가능하면 데모 경로를 직접 수행해. 결과를 PLAN.md에 기록해.
2. 그 다음 hackathon_reviewer subagent에게 현재 diff와 실행 증거를 읽기 전용으로 검토하게 해. 결과를 기다려.
3. reviewer의 각 finding을 네가 실제 코드와 재현 결과로 확인해. 근거 없는 finding은 기각 사유를 기록해.
4. 확인된 P0/P1만 우선순위대로 가장 작은 수정으로 해결하고, 실패한 좁은 검사부터 전체 검증까지 다시 실행해.
5. 수정 후 reviewer를 한 번 더 실행해 회귀를 확인해.

최대 3번의 fix cycle까지만 반복해. 이후에도 같은 문제가 남으면 자동 수정을 멈추고 문제, 시도, 실제 출력, 가장 작은 fallback을 제시해. 종료 조건은 P0/P1 0개, 핵심 데모의 실행 증거, PLAN.md 갱신이야.
```

