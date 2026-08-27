# Codex Hackathon Kit

하루짜리 해커톤에서 Codex를 `기획 → 병렬 구현 → 검증 → 데모 고정` 순서로 운영하기 위한 최소 구성입니다.

## 10분 시작 순서

1. [`SPEC.md`](SPEC.md)의 `TODO`를 팀과 함께 채운다.
2. 실제 프로젝트의 실행·검증 명령을 `SPEC.md`에 적는다.
3. Codex에서 [`prompts/00-kickoff.md`](prompts/00-kickoff.md)를 그대로 붙여 넣는다.
4. 생성된 계획을 확인하고 `GO`라고 답해 구현을 시작한다.
5. 첫 번째 수직 슬라이스가 동작하면 범위를 잠그고 [`HACKATHON_RUNBOOK.md`](HACKATHON_RUNBOOK.md)의 루프를 따른다.

## 파일 지도

| 파일 | 역할 |
| --- | --- |
| `SPEC.md` | 제품 범위, 90초 데모, 완료 조건의 단일 기준점 |
| `PLAN.md` | 작업 소유권, 의존성, 검증 증거를 기록하는 실행 보드 |
| `AGENTS.md` | 이 저장소에서 모든 Codex 작업에 적용되는 규칙 |
| `DEMO.md` | 실제 발표 대본, 복구 경로, 데모 체크리스트 |
| `HACKATHON_RUNBOOK.md` | 시간대별 운영 루프와 중단 규칙 |
| `.codex/agents/*.toml` | Planner, Frontend, Backend, Reviewer 역할 정의 |
| `prompts/*.md` | Codex에 그대로 붙여 넣는 단계별 명령 |

## 핵심 원칙

- 문서보다 동작하는 수직 슬라이스를 우선한다.
- 병렬 에이전트는 소유 파일이 겹치지 않을 때만 사용한다.
- 완료 판단은 에이전트의 설명이 아니라 실행한 명령과 실제 데모 결과로 한다.
- 전체 시간의 마지막 20%에는 새 기능을 추가하지 않는다.

