# AGENT MARKET 실행용 PRD (v1)

## 0. 문서 목적
이 문서는 **개발팀이 바로 구현 가능한 수준**으로 Agent Market(가칭)의 요구사항, 화면, API, 데이터 모델, 운영 정책을 정의한다.

---

## 1. 제품 목표
### 1.1 목표
- 사용자가 본인 OpenClaw를 토큰으로 안전하게 연동
- 에이전트 커스터마이징(페르소나/스타일/MD) 적용
- Skill/MD 상품을 거래하고 원클릭 설치

### 1.2 MVP 성공 기준 (출시 후 30일)
- 연동 계정 100개
- 등록 상품 50개
- 구매 전환율 5%+
- 설치 성공률 95%+
- 환불률 10% 이하

---

## 2. 사용자 및 역할
- **Buyer**: 상품 탐색/구매/설치
- **Creator**: 상품 등록/업데이트/가격 설정
- **Reviewer(Admin)**: 심사/승인/차단/분쟁 처리
- **Platform Admin**: 정책/수수료/정산 운영

---

## 3. MVP 범위
## 3.1 포함 (Must)
1) OpenClaw 연동 (토큰 저장/검증/회수)
2) 상품 등록/목록/상세/검색
3) 결제(테스트 결제 포함) + 주문 생성
4) 설치(특히 MD Pack) + 롤백
5) 리뷰/평점
6) 관리자 심사 플로우

## 3.2 제외 (Later)
- 추천 알고리즘 개인화
- 자동 성능 벤치마크 리포트
- 팀 단위 세분 권한관리

---

## 4. 핵심 사용자 플로우
## 4.1 Buyer 플로우
1. 회원가입/로그인
2. OpenClaw 토큰 연동
3. 마켓 탐색 → 상세 확인
4. 구매 → 내 라이브러리 추가
5. 설치 대상 에이전트 선택
6. 설치 실행 → 결과 확인
7. 필요 시 롤백

## 4.2 Creator 플로우
1. 크리에이터 등록
2. 상품 메타 입력 + 파일 업로드
3. 가격/라이선스 설정
4. 심사 요청
5. 승인 후 판매
6. 업데이트 버전 배포

## 4.3 Reviewer 플로우
1. 대기열 확인
2. 자동 검사 결과 확인
3. 수동 리뷰(정책/품질/보안)
4. 승인/반려 + 사유 작성

---

## 5. 정보 구조 (IA)
- Home
- Marketplace
  - 카테고리: 개발, 디자인, PM, 운영, Persona
- Product Detail
- Cart/Checkout
- My Library
- My OpenClaw Connections
- Creator Studio
- Admin Review Console

---

## 6. 화면 정의 (MVP)
1. `로그인/회원가입`
2. `OpenClaw 연동 관리`
3. `마켓 리스트`
4. `상품 상세`
5. `결제/주문 완료`
6. `내 라이브러리`
7. `설치/롤백 모달`
8. `리뷰 작성`
9. `크리에이터 상품 등록/수정`
10. `관리자 심사 대시보드`

각 화면 최소 컴포넌트:
- 제목/설명
- 핵심 CTA 1~2개
- 오류 상태/빈 상태
- 로딩 상태

---

## 7. 기능 요구사항 (Functional Requirements)
## 7.1 연동 관리
- FR-001: 사용자별 OpenClaw 연결 추가/삭제 가능
- FR-002: 토큰은 암호화 저장(AES-256)
- FR-003: 연결 테스트(health/ping) 버튼 제공
- FR-004: 토큰 rotate/revoke 이력 저장

## 7.2 상품
- FR-101: 상품 타입(Skill/MD/Persona) 선택
- FR-102: 버전(SemVer) 필수
- FR-103: 체인지로그 필수
- FR-104: 승인 전에는 비공개

## 7.3 구매/주문
- FR-201: 주문 상태(created/paid/refunded/failed)
- FR-202: 중복 구매 시 “업데이트 권한” 정책 적용

## 7.4 설치/롤백
- FR-301: 설치 전 영향 파일 목록 표시
- FR-302: 설치 전 스냅샷 생성
- FR-303: 실패 시 자동 롤백
- FR-304: 사용자 수동 롤백 지원

## 7.5 리뷰
- FR-401: 구매자만 리뷰 작성 가능
- FR-402: 별점(1~5), 텍스트 리뷰

## 7.6 심사
- FR-501: 자동 검사 통과 후 수동 심사 가능
- FR-502: 반려 사유 템플릿 제공

---

## 8. 비기능 요구사항 (NFR)
- NFR-01: 주요 API p95 800ms 이하
- NFR-02: 설치 성공률 95% 이상
- NFR-03: 감사 로그 90일 보관
- NFR-04: 민감 데이터 암호화 저장
- NFR-05: 에러 모니터링(Sentry) + 알림

---

## 9. 데이터 모델 (초안)
## 9.1 테이블
- `users` (id, email, role, created_at)
- `openclaw_connections` (id, user_id, name, endpoint, token_encrypted, scopes, status, last_checked_at)
- `products` (id, creator_id, type, title, description, price, currency, license, status)
- `product_versions` (id, product_id, version, package_url, checksum, changelog, review_status)
- `orders` (id, user_id, total_amount, status, payment_provider, paid_at)
- `order_items` (id, order_id, product_id, version_id, price)
- `installations` (id, user_id, connection_id, product_id, version_id, status, snapshot_id, installed_at)
- `rollback_histories` (id, installation_id, reason, rolled_back_at)
- `reviews` (id, user_id, product_id, rating, content, created_at)
- `audit_logs` (id, actor_id, action, target_type, target_id, metadata, created_at)

---

## 10. API 스펙 (MVP)
## 10.1 Auth
- `POST /api/auth/signup`
- `POST /api/auth/login`

## 10.2 Connection
- `POST /api/connections`
- `GET /api/connections`
- `POST /api/connections/:id/test`
- `POST /api/connections/:id/rotate`
- `DELETE /api/connections/:id`

## 10.3 Product
- `POST /api/products`
- `GET /api/products?type=&q=&sort=`
- `GET /api/products/:id`
- `POST /api/products/:id/versions`
- `POST /api/products/:id/submit-review`

## 10.4 Order
- `POST /api/orders`
- `POST /api/orders/:id/pay`
- `GET /api/orders/:id`

## 10.5 Install
- `POST /api/installations`
- `GET /api/installations?userId=`
- `POST /api/installations/:id/rollback`

## 10.6 Review/Admin
- `POST /api/reviews`
- `GET /api/admin/review-queue`
- `POST /api/admin/reviews/:id/approve`
- `POST /api/admin/reviews/:id/reject`

---

## 11. 보안 정책
1. 토큰 평문 저장 금지
2. 서버 비밀키 KMS/환경분리
3. 상품 패키지 checksum 검증
4. 설치 전 권한 안내 + 동의
5. 심사 실패 상품 자동 비노출
6. 비정상 설치 시 자동 차단/알림

---

## 12. 기술 스택 제안
- Frontend: Next.js (App Router)
- Backend: Next.js API + Worker
- DB: PostgreSQL
- Storage: S3 호환 스토리지
- Queue: Redis + BullMQ
- Auth: NextAuth/Clerk
- Payments: Stripe(초기)
- Observability: Sentry + OpenTelemetry

---

## 13. 개발 일정 (8주)
### 주 1~2: 설계/기반
- IA/와이어/DB/API 확정
- 인증/권한/연동 모듈 구축

### 주 3~4: 마켓 코어
- 상품/버전/검색/상세
- 심사 대기열 기본

### 주 5~6: 구매/설치
- 주문/결제
- 설치/스냅샷/롤백

### 주 7: 안정화
- QA, 보안 점검, 로깅 강화

### 주 8: 파일럿 런칭
- 초기 사용자 온보딩
- KPI 계측 및 개선 백로그 작성

---

## 14. QA 체크리스트
- [ ] 결제 성공/실패/취소 케이스
- [ ] 설치 성공/실패/타임아웃/롤백
- [ ] 권한 없는 사용자 접근 차단
- [ ] 악성/불완전 패키지 업로드 차단
- [ ] 관리자 승인/반려 로그 기록

---

## 15. 운영 정책
- 심사 SLA: 영업일 2일 내 1차 결과
- 환불 정책: 구매 후 7일, 미사용/중대 결함 우선
- 분쟁 처리: 증빙 기반 관리자 판정
- 불량 상품 누적 시 Creator 제재

---

## 16. 출시 직후 우선 개선 백로그
1. 설치 성공률 대시보드
2. 상품 품질 배지(검증됨/고성능)
3. 카테고리별 추천 랭킹
4. 팀 플랜(워크스페이스 공유 라이브러리)

---

## 17. 오너십 (R&R)
- PM: 요구사항/우선순위/지표
- FE: 마켓/라이브러리/설치 UI
- BE: 연동/주문/설치 엔진/로그
- Sec/Review: 정책/심사/취약점 대응
- Design: UX, 템플릿, 크리에이터 가이드

---

## 18. 즉시 실행 To-do (이번 주)
1. 테이블 스키마 확정 회의 (2시간)
2. 설치 엔진 인터페이스 명세 작성
3. 심사 정책 문서(허용/금지 사례) 작성
4. 와이어프레임 10개 화면 확정
5. 파일럿 Creator 5명 모집
