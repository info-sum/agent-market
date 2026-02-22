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

## Next implementation
- Auth/JWT
- Connection APIs
- Product/Order/Install APIs
- Alembic migrations from `docs/AGENT_MARKET_DB_SCHEMA_v1.sql`
