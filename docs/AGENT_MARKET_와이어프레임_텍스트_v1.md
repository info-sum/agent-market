# AGENT MARKET 화면별 와이어프레임 (텍스트) v1

## Screen 01. 로그인/회원가입
- Header: 로고, 언어 선택
- Body:
  - 이메일
  - 비밀번호
  - [로그인]
  - [회원가입 전환]
- Footer: 약관/개인정보
- 상태: 로그인 실패 에러 배너

## Screen 02. OpenClaw 연동 관리
- Header: "내 OpenClaw 연결"
- List Card(반복): 이름, endpoint, 상태(active/invalid), 마지막 체크 시간
- CTA:
  - [연결 추가]
  - [연결 테스트]
  - [토큰 교체]
  - [연결 삭제]
- Modal(연결 추가): name, endpoint, token, scope 체크박스

## Screen 03. 마켓 리스트
- Top: 검색창, 카테고리 탭(개발/디자인/PM/Persona)
- Filter: 가격, 평점, 최신순/인기순
- Product Card:
  - 썸네일
  - 제목
  - 타입 배지(Skill/MD/Persona)
  - 가격
  - 평점/리뷰 수
  - [상세보기]
- Empty: "조건에 맞는 상품이 없습니다"

## Screen 04. 상품 상세
- 좌측: 상품 설명, 버전 탭, 체인지로그
- 우측: 가격, 라이선스, 판매자 정보, 평점
- CTA:
  - [장바구니]
  - [바로 구매]
- 하단: 리뷰 목록 + [리뷰 작성]

## Screen 05. 결제/주문 완료
- Order Summary: 상품명/버전/금액
- 결제 수단 선택
- CTA:
  - [결제하기]
- 완료 상태:
  - "결제 완료"
  - [내 라이브러리로 이동]

## Screen 06. 내 라이브러리
- 탭: 전체/설치 가능/설치됨
- Item:
  - 상품명
  - 보유 버전
  - 업데이트 여부
  - [설치]
  - [설치 이력]

## Screen 07. 설치/롤백 모달
- Step 1: 대상 연결(OpenClaw) 선택
- Step 2: 설치 영향 파일 목록 표시
- Step 3: 동의 체크 + [설치 실행]
- Result:
  - 성공: snapshot id 표시 + [닫기]
  - 실패: 에러 + [자동 롤백 실행]
- 별도 CTA: [이전 버전으로 롤백]

## Screen 08. 리뷰 작성
- 입력: 별점(1~5), 텍스트
- CTA: [등록]
- 제한: 구매자만 가능 안내

## Screen 09. Creator Studio (상품 등록/수정)
- 상품 기본정보: 타입, 제목, 설명, 카테고리
- 가격/라이선스
- 버전 등록:
  - version
  - package URL
  - checksum
  - changelog
- CTA:
  - [임시저장]
  - [심사 요청]
- 상태 배지: draft/pending/approved/rejected

## Screen 10. Admin Review Console
- 탭: 대기중/승인/반려
- Queue Row:
  - 상품명/버전/판매자
  - 자동검사 결과(pass/fail)
  - 위험도
  - [상세]
- 상세 패널:
  - 패키지 메타/체인지로그/권한 영향
  - [승인]
  - [반려]
  - 반려 사유 템플릿

---

## 공통 UI 상태 가이드
- Loading: 스켈레톤 3~6개
- Error: 재시도 버튼 + 에러코드
- Empty: 다음 액션 CTA 노출
- Permission Denied: 권한 요청 안내

## 공통 내비게이션
- 좌측 사이드바: Marketplace / My Library / Connections / Creator Studio / Admin
- 우측 상단: 알림 / 프로필 / 로그아웃
