# Agent Market

OpenClaw 사용자들이 자신의 에이전트를 연동하고, 커스터마이징 자산(Persona/MD/Skill)을 사고팔 수 있는 플랫폼 프로젝트입니다.

## 프로젝트 구조
- `frontend/` : Frontend (Next.js 예정)
- `backend/` : Backend (FastAPI)
- `docs/` : 기획/PRD/스키마/API/정책 문서
- `infra/` : 로컬 인프라 (docker-compose)

## 문서 빠른 시작
- 기획서: `docs/AGENT_MARKET_기획서_v1.md`
- 실행 PRD: `docs/AGENT_MARKET_PRD_실행용_v1.md`
- DB 스키마: `docs/AGENT_MARKET_DB_SCHEMA_v1.sql`
- API 스펙: `docs/AGENT_MARKET_OPENAPI_v1.yaml`
- 화면 와이어프레임: `docs/AGENT_MARKET_와이어프레임_텍스트_v1.md`
- 개발 로드맵: `docs/ROADMAP.md`
- 스프린트 백로그: `docs/MVP_BACKLOG.md`
- 보안 정책: `docs/SECURITY.md`
- 심사 정책: `docs/REVIEW_POLICY.md`
- 크리에이터 가이드: `docs/CREATOR_GUIDE.md`

## 프로젝트 목표 (MVP)
1. OpenClaw 토큰 연동
2. 상품 등록/탐색/구매
3. MD Pack 설치/롤백
4. 관리자 심사 플로우

## 권장 스택
- Frontend: Next.js
- Backend: FastAPI + Worker
- DB: PostgreSQL
- Queue: Redis + BullMQ
- Monitoring: Sentry

## 로컬 개발 예정 명령 (초안)
```bash
# 추후 앱 초기화 후 사용
# npm install
# npm run dev
```

## 브랜치 전략 (초안)
- `master`: 안정 브랜치
- `feature/*`: 기능 작업
- `hotfix/*`: 긴급 수정

## 라이선스
TBD
