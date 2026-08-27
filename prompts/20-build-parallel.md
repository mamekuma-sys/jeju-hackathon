# Build and integration prompt

```text
SPEC.md와 승인된 PLAN.md의 P0 수직 슬라이스를 구현해줘. .agents/agents/frontend-builder.md와 backend-builder.md의 역할 계약을 사용해.

1. 먼저 shared contract와 서로 겹치지 않는 소유 경로를 다시 확인해.
2. 현재 도구가 네이티브 하위 에이전트를 지원하고 독립적인 Frontend/Backend 작업이 모두 존재하면 두 Builder를 병렬 실행해.
3. 네이티브 위임은 없지만 병렬 세션/Worktree가 있으면 각 세션에 정확한 task ID, acceptance criteria, owned paths, 금지 경로, shared contract, 검증 명령과 해당 역할 파일을 전달해.
4. 위 두 방식이 없거나 경로가 겹치면 같은 역할을 순차 실행해. 억지로 병렬화하지 마.
5. 모든 결과를 기다리고 실제 diff를 검토해. shared config, lockfile, contract 조정, 통합은 Coordinator가 직접 소유해.
6. 좁은 테스트부터 전체 lint/typecheck/test/build, 핵심 smoke flow 순으로 실행해.
7. UI가 있으면 가능한 브라우저/컴퓨터 사용 도구로 실제 90초 데모 경로와 loading/error 상태를 확인해.
8. PLAN.md에 상태와 정확한 verification evidence를 기록해.

P0 수직 슬라이스가 검증될 때까지 범위 안에서 수정하되, 같은 실패가 3회 반복되면 멈추고 원인·증거·가장 작은 fallback을 보고해. 완료 보고에는 변경 파일, 실행한 명령/동작, 결과, 남은 위험을 포함해.
```

