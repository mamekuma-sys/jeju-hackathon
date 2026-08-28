# Planner prompt

```text
AGENTS.md, SPEC.md, PLAN.md, RUNTIME_CONTRACT.md와 .agents/agents/planner.md를 읽고 구현 전 계획을 만들어줘. 아직 코드를 수정하지 마.

Single Coordinator를 기본값으로 두고 다음을 반환해:
- Blocker와 안전한 가정
- 가장 작은 end-to-end 수직 슬라이스
- task ID, priority, owner, dependencies, owned/forbidden paths, done condition, verification, stop condition
- request/response/error/sample 계약
- 저장소에서 실제로 확인한 install/dev/lint/typecheck/test/build/smoke 명령
- 외부 효과와 필요한 승인
- 위험 5개와 fallback

병렬 worker는 AGENTS.md의 Gate를 모두 통과할 때만 제안해. 결과를 저장소와 대조한 뒤 Coordinator가 PLAN.md에 반영하고 GO/NO-GO를 알려줘.
```

