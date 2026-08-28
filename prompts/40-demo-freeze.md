# Demo freeze prompt

```text
지금부터 demo freeze야. 새 기능, 새 의존성, 큰 리팩터링은 금지하고 P0/P1 데모 결함만 수정해.

1. known-good commit과 실행 환경을 기록해.
2. SPEC.md와 DEMO.md에 선언된 Representative demo path를 clean start에서 세 번 실행하고 매번 Demo timebox 안에 들어오는지 확인해.
3. 각 회차의 대상 commit, 시간, 성공/실패, 증거를 DEMO.md와 PLAN.md에 기록해.
4. 외부 API fallback과 배포 실패 localhost fallback을 각각 한 번 검증해.
5. README setup, 비밀값 노출, 외부 effect ledger를 점검해.
6. 같은 외부 작업을 다시 실행하지 말고 원격 상태를 먼저 확인해.

P2/P3는 목록만 남겨. 마지막에 발표 직전 체크리스트, Demo timebox, 실행 명령, URL, seeded/live demo data 구분, fallback 전환 방법을 한 화면 분량으로 요약해.
```
