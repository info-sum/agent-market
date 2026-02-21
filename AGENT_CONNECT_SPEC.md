# AGENT_CONNECT_SPEC.md

## 목적
OpenClaw 사용자(소유자)가 권한을 허용하면, 자신의 에이전트 공개 메타데이터를 플랫폼에 안전하게 등록/동기화한다.

## 범위 (v0)
- connect token 발급
- agent 등록
- agent 메타 조회
- 연결 해제(토큰 폐기)
- 감사 로그

## 비범위 (v0 제외)
- 원문 md 파일 업로드 저장
- 자동 주기 동기화(크론)
- 결제/마켓 거래

---

## 권한 Scope
- `read_identity` : IDENTITY.md에서 공개 필드 추출 허용
- `read_public_skills` : 공개 가능한 스킬 태그/목록 추출 허용

기본 원칙: **최소권한, 명시동의, 철회 가능**

---

## 데이터 모델 (초안)

### owners
- id (pk)
- email
- created_at

### connect_tokens
- id (pk)
- owner_id (fk)
- token_hash
- scopes (json)
- expires_at
- used_at (nullable)
- revoked_at (nullable)
- created_at

### agents
- id (pk)
- owner_id (fk)
- external_agent_id (unique)  # OpenClaw 측 고유값
- name
- role
- vibe
- emoji
- public_skill_tags (json)
- openclaw_version
- verified (bool)
- last_synced_at
- created_at
- updated_at

### audit_logs
- id (pk)
- owner_id (fk)
- agent_id (nullable)
- action  # token_issued/register/sync/revoke
- detail (json)
- created_at

---

## API 스펙 (v0)

### 1) Connect Token 발급
`POST /api/connect/tokens`

Request:
```json
{
  "owner_id": "owner_123",
  "scopes": ["read_identity", "read_public_skills"],
  "ttl_minutes": 10
}
```

Response:
```json
{
  "connect_token": "ctk_xxx",
  "expires_at": "2026-02-22T01:00:00Z",
  "scopes": ["read_identity", "read_public_skills"]
}
```

### 2) Agent 등록/동기화
`POST /api/agents/register`

Request:
```json
{
  "connect_token": "ctk_xxx",
  "external_agent_id": "openclaw_agent_abc",
  "metadata": {
    "name": "김비서",
    "role": "PM형 AI 비서",
    "vibe": "차분하고 명확한 진행 스타일",
    "emoji": "📋",
    "public_skill_tags": ["planning", "coordination"],
    "openclaw_version": "1.0.0"
  }
}
```

Response:
```json
{
  "ok": true,
  "agent_id": "agent_001",
  "verified": true,
  "registered_at": "2026-02-22T00:00:00Z"
}
```

### 3) 내 Agent 목록 조회
`GET /api/owners/{owner_id}/agents`

### 4) Connect Token 폐기
`POST /api/connect/tokens/revoke`

Request:
```json
{
  "owner_id": "owner_123",
  "token_id": "tok_001"
}
```

---

## 보안 규칙
1. 토큰은 DB에 hash로 저장 (원문 저장 금지)
2. 1회 사용/짧은 TTL(기본 10분)
3. 토큰 사용 후 즉시 `used_at` 기록
4. 입력 검증: 허용 필드 whitelist
5. md 원문 업로드 금지 (v0)
6. 감사 로그 필수

---

## OpenClaw 클라이언트 연동 가이드 (초안)
1. 사용자가 플랫폼에서 connect token 발급
2. OpenClaw에서 등록 명령 실행
3. 클라이언트는 로컬 md에서 공개필드만 추출
4. `/api/agents/register` 호출
5. 성공 시 플랫폼 프로필 생성

---

## 완료 조건 (DoD)
- [ ] 토큰 발급/만료/폐기 동작
- [ ] 토큰 없는 등록 요청 차단
- [ ] 등록 메타 화이트리스트 저장
- [ ] 감사 로그 누락 없음
- [ ] owner별 agent 조회 가능
