# Universal AI Agent Hackathon Kit

하루짜리 해커톤에서 어떤 AI 코딩 에이전트를 사용하든 `기획 → 구현 → 검증 → 데모 고정` 순서로 운영하기 위한 공급자 중립 키트입니다. 분업은 독립 작업이 실제로 있을 때만 선택합니다.

CLI, IDE, 호스팅형 에이전트, 터미널 에이전트, 멀티에이전트 오케스트레이터 등 제품과 실행 환경이 달라도 핵심 문서와 프롬프트는 그대로 사용합니다. 특정 도구의 네이티브 기능은 편의 기능일 뿐 필수 조건이 아닙니다. 구체적인 연결 예시는 [`AGENT_COMPATIBILITY.md`](AGENT_COMPATIBILITY.md)에만 격리했습니다.

## 10분 시작 순서

1. [`SPEC.md`](SPEC.md)의 제품·데모 관련 `TODO`를 채운다.
2. 실제 프로젝트의 실행·검증 명령을 `SPEC.md`에 적는다.
3. 사용 중인 에이전트에서 [`prompts/00-kickoff.md`](prompts/00-kickoff.md)를 붙여 넣는다.
4. 생성된 계획을 확인하고 `GO`라고 답해 구현을 시작한다.
5. 첫 번째 수직 슬라이스가 동작하면 범위를 잠그고 [`HACKATHON_RUNBOOK.md`](HACKATHON_RUNBOOK.md)를 따른다.

## 세 가지 실행 모드

현재 도구가 지원하는 가장 높은 모드가 아니라, 작업을 끝낼 수 있는 가장 단순한 모드를 사용합니다.

| 모드 | 사용 조건 | 운영 방법 |
| --- | --- | --- |
| Single Coordinator (기본값) | 대부분의 기능 구현 | 한 에이전트가 계획·구현·검증하고 필요할 때만 역할 전환 |
| Read-only delegation | 탐색/리뷰 출력이 메인 컨텍스트를 오염시킴 | Planner 또는 Reviewer만 별도 읽기 전용 컨텍스트 사용 |
| Parallel workers | 독립 P0/P1 작업, 고정 계약, 비중첩 경로가 모두 충족 | 세션/Worktree마다 하나의 task packet을 할당하고 Coordinator가 통합 |

멀티에이전트는 기본 아키텍처가 아니라 지연시간 최적화입니다. 병렬 조건이 하나라도 불충분하면 Single Coordinator로 실행합니다.

## 파일 지도

| 파일 | 역할 |
| --- | --- |
| `SPEC.md` | 제품 범위, 90초 데모, 완료 조건의 단일 기준점 |
| `PLAN.md` | 작업 소유권, 의존성, 검증 증거를 기록하는 실행 보드 |
| `AGENTS.md` | 여러 도구가 공유하는 최상위 프로젝트 규칙 |
| `RUNTIME_CONTRACT.md` | 입력·상태·도구 결과·승인·재시도 계약 |
| `EVALS.md` | 해커톤 중 반복 실행할 최소 실패 시나리오 |
| `ARCHITECTURE_REVIEW.md` | 현재 구조의 A–J 리뷰와 수정 근거 |
| `.agents/agents/*.md` | 공급자 중립 Planner, Frontend, Backend, Reviewer 역할 원본 |
| `prompts/*.md` | 어떤 에이전트 채팅에도 붙여 넣을 수 있는 단계별 명령 |
| `AGENT_COMPATIBILITY.md` | 도구별 자동 로딩 파일과 수동 사용법 |
| `CLAUDE.md`, `GEMINI.md` 등 | 공통 규칙으로 연결하는 얇은 호환 어댑터 |
| `.codex/`, `.claude/` | 네이티브 역할 호출을 위한 선택적 제품 어댑터 |
| `DEMO.md` | 실제 발표 대본, 복구 경로, 데모 체크리스트 |
| `HACKATHON_RUNBOOK.md` | 시간대별 운영 루프와 중단 규칙 |

## 핵심 원칙

- 제품 이름 대신 `역할 / 입력 / 출력 / 권한 / 완료 조건`으로 에이전트를 정의한다.
- 문서보다 동작하는 수직 슬라이스를 우선한다.
- 병렬 쓰기는 파일 소유권이 겹치지 않을 때만 사용한다.
- 완료 판단은 에이전트의 설명이 아니라 실행한 명령과 실제 데모 결과로 한다.
- Builder와 Reviewer의 컨텍스트를 가능한 한 분리한다.
- `PLAN.md`는 Coordinator만 수정한다. 다른 역할은 구조화된 handoff만 반환한다.
- 전체 시간의 마지막 20%에는 새 기능을 추가하지 않는다.

## 구조 자체 검증

```bash
python3 scripts/check-agent-kit.py
```

`SPEC.md`의 모든 필수 입력까지 검사하려면 다음을 사용합니다.

```bash
python3 scripts/check-agent-kit.py --strict
```
