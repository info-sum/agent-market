# Backend (FastAPI)

## Run locally
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Endpoints
- GET `/` - service status
- GET `/api/v1/health` - health check
- POST `/api/v1/auth/register`
- POST `/api/v1/auth/login`
- GET `/api/v1/auth/me`
- GET/POST `/api/v1/connections` (인증 필요)
- GET `/api/v1/products` (공개)
- POST `/api/v1/products` (인증 필요)
- GET/POST `/api/v1/installations` (인증 필요)

## Security Defaults
- 비밀번호 해시 저장(passlib+bcrypt)
- JWT Bearer 인증
- CORS origin 환경변수 설정 가능 (`CORS_ORIGINS`)
- `.env`에서 `JWT_SECRET` 반드시 교체 필요

## Prototype Notes
- 현재는 SQLite 기반 데모입니다. (`agent_market.db`)
- 서버 재시작 후에도 데이터가 유지됩니다.
- 프론트 데모(`../frontend/index.html`)와 함께 사용하면 연결/상품/설치 흐름을 빠르게 검증할 수 있습니다.

## Next implementation
- Alembic 마이그레이션
- 주문/결제/심사 API
- 권한(role) 분리
