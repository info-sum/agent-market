# ARCHITECTURE (MVP)

## 개요
Agent Market은 Web App + API + Worker + DB + Storage + Queue 구조로 동작한다.

## 컴포넌트
1. Web App (Next.js)
   - 마켓, 라이브러리, 크리에이터 스튜디오, 관리자 콘솔
2. API Server
   - 인증, 상품, 주문, 설치 요청, 심사 엔드포인트
3. Installation Worker
   - 설치 작업 큐 소비
   - 스냅샷/롤백 실행
4. PostgreSQL
   - 사용자/상품/주문/설치/로그 저장
5. Object Storage (S3 호환)
   - 패키지 파일 저장
6. Redis + BullMQ
   - 설치/검사 비동기 작업

## 시퀀스 (구매→설치)
1) 사용자 결제 완료
2) 주문 상태 paid 전환
3) 설치 요청 생성 (queued)
4) Worker가 작업 수행
5) 성공 시 installed, 실패 시 failed + rollback

## 신뢰성 설계
- 설치 작업 idempotency key
- 재시도 정책(최대 3회)
- 실패 원인 구조화(error_code, message)

## 관측성
- API 에러/성능: Sentry, OTel
- 비즈니스 이벤트: purchase_completed, install_succeeded 등
