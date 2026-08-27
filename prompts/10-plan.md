# Planner prompt

```text
AGENTS.md와 SPEC.md를 기준으로 구현 전 계획을 만들어줘. hackathon_planner subagent를 사용하고 결과를 기다려.

실제 저장소를 확인해서 다음을 반환해:
- SPEC의 모순, 남은 TODO, 결정이 필요한 항목
- 가장 작은 end-to-end 수직 슬라이스
- ID, 우선순위, 담당 역할, 의존성, 정확한 소유 경로, 관찰 가능한 완료 조건이 있는 작업 목록
- Frontend/Backend 공유 request/response/error 계약과 sample payload
- 저장소에서 확인한 install/dev/lint/typecheck/test/build/smoke 명령
- 상위 위험 5개와 각각의 fallback

병렬 쓰기는 소유 경로가 겹치지 않을 때만 제안하고 shared config, lockfile, 공용 계약 파일, 통합은 primary agent 소유로 남겨. 결과를 실제 저장소와 대조한 뒤 PLAN.md를 갱신해. 아직 기능은 구현하지 마. 마지막에 GO/NO-GO와 이유를 알려줘.
```

