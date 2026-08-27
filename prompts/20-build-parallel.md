# Parallel build prompt

```text
SPEC.md와 승인된 PLAN.md의 P0 수직 슬라이스를 구현해줘.

1. 먼저 shared contract와 각 agent의 서로 겹치지 않는 소유 경로를 다시 확인해.
2. 독립적인 Frontend/Backend 작업이 모두 존재할 때만 frontend_builder와 backend_builder를 병렬로 실행해. 각 agent에게 정확한 PLAN task ID, acceptance criteria, owned paths, 금지 경로, shared contract, 실행할 검증 명령을 전달해.
3. 둘 중 한 역할이 필요 없거나 경로가 겹치면 억지로 병렬화하지 말고 primary agent가 순서대로 처리해.
4. 모든 subagent 결과를 기다리고 실제 diff를 검토해. shared config, lockfile, contract 조정, 통합은 네가 직접 소유해.
5. 좁은 테스트부터 전체 lint/typecheck/test/build, 핵심 smoke flow 순으로 실행해.
6. UI가 있으면 가능한 browser 도구로 실제 90초 데모 경로와 loading/error 상태를 확인해.
7. PLAN.md에 상태와 정확한 verification evidence를 기록해.

P0 수직 슬라이스가 검증될 때까지 범위 안에서 수정하되, 같은 실패가 3회 반복되면 멈추고 원인·증거·가장 작은 fallback을 보고해. 완료 보고에는 변경 파일, 실행한 명령/동작, 결과, 남은 위험을 포함해.
```

