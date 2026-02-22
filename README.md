# Agent Market

OpenClaw 사용자들이 자신의 에이전트를 연동하고, 커스터마이징 자산(Persona/MD/Skill)을 사고팔 수 있는 플랫폼 프로젝트입니다.

## 문서 빠른 시작
- 기획서: `AGENT_MARKET_기획서_v1.md`
- 실행 PRD: `AGENT_MARKET_PRD_실행용_v1.md`
- DB 스키마: `AGENT_MARKET_DB_SCHEMA_v1.sql`
- API 스펙: `AGENT_MARKET_OPENAPI_v1.yaml`
- 화면 와이어프레임: `AGENT_MARKET_와이어프레임_텍스트_v1.md`
- 개발 로드맵: `ROADMAP.md`
- 스프린트 백로그: `MVP_BACKLOG.md`
- 보안 정책: `SECURITY.md`
- 심사 정책: `REVIEW_POLICY.md`
- 크리에이터 가이드: `CREATOR_GUIDE.md`

## 프로젝트 목표 (MVP)
1. OpenClaw 토큰 연동
2. 상품 등록/탐색/구매
3. MD Pack 설치/롤백
4. 관리자 심사 플로우

## 권장 스택
- Frontend: Next.js
- Backend: Next.js API + Worker
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
