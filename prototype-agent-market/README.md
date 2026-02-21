# OpenClaw Agent Market Prototype (FE/BE 분리)

OpenSea 벤치마킹 구조를 기반으로 만든 최소 기능 프로토타입.

## 구조

- `backend/` FastAPI API 서버
- `frontend/` 정적 웹 프론트엔드 (Vanilla JS)

## 실행 방법

### 1) Backend 실행

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### 2) Frontend 실행

새 터미널:

```bash
cd frontend
python3 -m http.server 5173
```

브라우저에서 `http://localhost:5173` 접속.

## 제공 기능 (Prototype)

- Collection 카드(바닥가/거래량)
- Skill 리스트/검색/필터/정렬
- Skill 상세 정보 카드(검증 상태/호환 버전/평점)
- 구매 버튼(모의 구매, 설치 수 증가)
- Agent 쇼케이스

## API 목록

- `GET /health`
- `GET /api/collections`
- `GET /api/agents`
- `GET /api/skills`
- `GET /api/skills/{skill_id}`
- `POST /api/skills/{skill_id}/purchase`

## 다음 단계 권장

1. DB 연동(PostgreSQL) + 영속 저장
2. 사용자 인증 및 주문 이력
3. 스킬 검증 워커(권한/호환성 자동체크)
4. 판매자 등록/버전 업로드 UI
