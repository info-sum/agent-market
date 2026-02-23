# PROGRESS LOG

최종 업데이트: 2026-02-23 (KST)

## 1) 프로젝트 방향 합의
- 프로젝트: **Agent Market**
- 목표:
  - 사용자별 OpenClaw를 토큰 방식으로 웹에 연동
  - 에이전트 커스터마이징(페르소나/스타일/"옷입히기")
  - Skill/MD/Persona 자산 거래 마켓 구축
- 아키텍처 방향: **Frontend / Backend 분리**
- 백엔드 기술: **FastAPI**

---

## 2) 작성/정리한 문서
초기 문서 작성 후 `docs/`로 정리 완료.

- `docs/AGENT_MARKET_기획서_v1.md`
- `docs/AGENT_MARKET_PRD_실행용_v1.md`
- `docs/AGENT_MARKET_DB_SCHEMA_v1.sql`
- `docs/AGENT_MARKET_OPENAPI_v1.yaml`
- `docs/AGENT_MARKET_와이어프레임_텍스트_v1.md`
- `docs/ARCHITECTURE.md`
- `docs/ROADMAP.md`
- `docs/MVP_BACKLOG.md`
- `docs/SECURITY.md`
- `docs/REVIEW_POLICY.md`
- `docs/CREATOR_GUIDE.md`

루트 문서:
- `README.md`
- `.gitignore`

---

## 3) 리포지토리/GitHub 작업
- 원격 연결: `https://github.com/info-sum/agent-market.git`
- branch: `master`
- 다수 문서 커밋/푸시 완료
- 구조 변경 커밋 완료 (frontend/backend/docs/infra 분리)

---

## 4) 현재 코드 구조
- `frontend/`
  - `index.html` (프로토타입 데모 UI)
  - `README.md`
- `backend/`
  - `app/main.py`
  - `app/api/v1/health.py`
  - `app/api/v1/prototype.py`
  - `app/schemas/prototype.py`
  - `app/services/prototype_store.py` (초기 인메모리 스토어)
  - `app/db.py` (SQLAlchemy 엔진/세션)
  - `app/models.py` (Connection/Product/Installation)
  - `app/core/config.py`
  - `requirements.txt`
  - `.env.example`
  - `README.md`
- `infra/`
  - `docker-compose.yml` (postgres/redis)

---

## 5) 구현 상태 (프로토타입)
### 완료
- FastAPI 기본 서버 구성
- Health 체크 엔드포인트
- Prototype API:
  - `GET/POST /api/v1/connections`
  - `GET/POST /api/v1/products`
  - `GET/POST /api/v1/installations`
- CORS 허용
- 프론트 데모 페이지에서
  - 연결 추가
  - 상품 조회
  - 설치 실행
  - 상태 확인 가능

### 진행 중/최근 변경
- 인메모리 방식에서 DB 영속화로 전환 작업 진행
- 기본 DB를 SQLite로 설정 (`sqlite:///./agent_market.db`)
- startup 시 테이블 생성 + 기본 상품 seed 로직 반영

---

## 6) 운영 이슈 기록
### 텔레그램 연동
- 채널 설정은 존재하나 probe 실패 지속
- 로그: `setMyCommands/deleteMyCommands network request failed`
- 네트워크 접근(curl) 자체는 응답 확인
- 토큰 재등록/게이트웨이 재시작/업데이트 진행
- 상태: **미해결(재점검 필요)**

### 메모리 검색
- memory_search 임베딩 쿼터 초과(429)로 비활성 상태 발생
- 상태: **외부 쿼터 이슈로 제한적 사용**

---

## 7) 다음 액션 (개발 우선)
1. Backend
   - Auth/JWT
   - 라우터 구조 정식화 (connections/products/installations)
   - Alembic 마이그레이션 세팅
2. Frontend
   - Next.js 전환
   - 화면 분리: 마켓/상세/라이브러리/연동관리
3. Infra
   - 로컬 실행 스크립트 정리
   - env 템플릿 확정
4. QA
   - API smoke test
   - 설치 실패/롤백 시나리오

---

## 8) 추가 개발 진행 (보안 + 트렌디 UI)
요청: "보안 신경써서 개발 + 트렌디한 UI/UX"

### 백엔드 보안 기능 추가
- 인증 스키마 추가: `backend/app/schemas/auth.py`
- 보안 유틸 추가: `backend/app/core/security.py`
  - bcrypt 비밀번호 해시/검증
  - JWT 발급/검증
- 인증 의존성 추가: `backend/app/deps.py`
  - Bearer 토큰 기반 현재 사용자 조회
- 인증 라우터 추가: `backend/app/api/v1/auth.py`
  - `POST /auth/register`
  - `POST /auth/login`
  - `GET /auth/me`
- 모델 확장: `backend/app/models.py`
  - `users` 테이블
  - `connections/installations`에 owner_id 추가
- prototype API 접근 정책 강화
  - 연결/설치 조회는 로그인 사용자 소유 데이터만
  - 생성 API 대부분 인증 필요
- 설정 확장
  - `JWT_SECRET`, `JWT_ALGORITHM`, `CORS_ORIGINS` 추가

### 프론트 UI/UX 개선
- `frontend/index.html` 전면 개선
  - 다크 그라디언트 기반 트렌디 대시보드
  - 인증 섹션(회원가입/로그인)
  - 연결/상품/설치 섹션 구조화
  - 상태 패널 개선
  - 토큰 localStorage 유지

### 문서 업데이트
- `backend/README.md` 보안/엔드포인트 최신화
- `frontend/README.md` 기능/방향 최신화

---

## 9) 요청 반영 규칙
사용자 요청: "진행 상황 다 MD 파일로 저장"
- 본 파일(`PROGRESS_LOG.md`)을 기준으로 지속 업데이트.
- 큰 작업 완료 시마다 섹션 추가/갱신.
