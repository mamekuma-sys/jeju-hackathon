# Demo freeze prompt

```text
지금부터 demo freeze야. 새 기능, 새 의존성, 큰 리팩터링은 금지하고 P0/P1 데모 결함만 수정해.

1. SPEC.md와 DEMO.md의 90초 경로를 clean start에서 세 번 실행해.
2. 각 회차의 시간, 성공/실패, 관찰한 문제를 DEMO.md에 기록해.
3. 외부 API 실패 fallback과 배포 실패 localhost fallback을 각각 한 번 검증해.
4. README의 setup 명령을 새 환경 관점에서 점검하고 비밀값 노출 여부를 확인해.
5. 현재 known-good git 상태를 기록해.

발견한 P2/P3는 고치지 말고 목록만 남겨. P0/P1 수정은 최소 변경 후 실패한 검사와 전체 데모를 다시 실행해. 마지막에 발표 직전 체크리스트, 실행 명령, URL, demo data, fallback 전환 방법을 한 화면 분량으로 요약해.
```
