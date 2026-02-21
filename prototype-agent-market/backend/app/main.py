from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="OpenClaw Agent Market Prototype")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Skill(BaseModel):
    id: str
    name: str
    category: str
    owner_agent: str
    price: int
    verified: str  # unverified | basic | compatibility
    installs: int
    rating: float
    description: str
    openclaw_version: str


class Agent(BaseModel):
    id: str
    name: str
    specialty: str
    followers: int
    avatar: str


class Collection(BaseModel):
    id: str
    name: str
    floor_price: int
    volume_7d: int


SKILLS: List[Skill] = [
    Skill(
        id="skill-dev-001",
        name="Code Review Copilot Pack",
        category="development",
        owner_agent="백엔",
        price=29000,
        verified="compatibility",
        installs=182,
        rating=4.8,
        description="Pull request 리뷰 자동 체크 + 리스크 하이라이트",
        openclaw_version=">=1.6",
    ),
    Skill(
        id="skill-plan-002",
        name="PRD Sprint Planner",
        category="planning",
        owner_agent="프엔",
        price=19000,
        verified="basic",
        installs=96,
        rating=4.6,
        description="요구사항을 스프린트 백로그로 분해하고 우선순위 자동 추천",
        openclaw_version=">=1.5",
    ),
    Skill(
        id="skill-qa-003",
        name="Regression Test Pilot",
        category="qa",
        owner_agent="큐에",
        price=24000,
        verified="compatibility",
        installs=130,
        rating=4.7,
        description="핵심 사용자 플로우 기반 회귀 테스트 시나리오 자동 생성",
        openclaw_version=">=1.6",
    ),
]

AGENTS: List[Agent] = [
    Agent(id="agent-be", name="백엔", specialty="API/아키텍처", followers=320, avatar="🛠️"),
    Agent(id="agent-fe", name="프엔", specialty="UI/UX", followers=275, avatar="🎨"),
    Agent(id="agent-qa", name="큐에", specialty="품질/테스트", followers=211, avatar="🧪"),
]

COLLECTIONS: List[Collection] = [
    Collection(id="col-dev", name="Development Masters", floor_price=19000, volume_7d=940000),
    Collection(id="col-plan", name="Planning Experts", floor_price=12000, volume_7d=510000),
    Collection(id="col-qa", name="QA Guardians", floor_price=15000, volume_7d=430000),
]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/api/collections", response_model=List[Collection])
def list_collections():
    return COLLECTIONS


@app.get("/api/agents", response_model=List[Agent])
def list_agents():
    return AGENTS


@app.get("/api/skills", response_model=List[Skill])
def list_skills(
    category: Optional[str] = None,
    verified: Optional[str] = None,
    q: Optional[str] = None,
    sort: Optional[str] = "popular",
):
    result = SKILLS

    if category:
        result = [s for s in result if s.category == category]
    if verified:
        result = [s for s in result if s.verified == verified]
    if q:
        keyword = q.lower()
        result = [s for s in result if keyword in s.name.lower() or keyword in s.description.lower()]

    if sort == "price_asc":
        result = sorted(result, key=lambda s: s.price)
    elif sort == "price_desc":
        result = sorted(result, key=lambda s: s.price, reverse=True)
    elif sort == "rating":
        result = sorted(result, key=lambda s: s.rating, reverse=True)
    else:  # popular
        result = sorted(result, key=lambda s: s.installs, reverse=True)

    return result


@app.get("/api/skills/{skill_id}", response_model=Skill)
def get_skill(skill_id: str):
    for s in SKILLS:
        if s.id == skill_id:
            return s
    raise HTTPException(status_code=404, detail="Skill not found")


@app.post("/api/skills/{skill_id}/purchase")
def purchase_skill(skill_id: str):
    for i, s in enumerate(SKILLS):
        if s.id == skill_id:
            updated = s.model_copy(update={"installs": s.installs + 1})
            SKILLS[i] = updated
            return {
                "ok": True,
                "message": f"{s.name} 구매 완료 (Prototype)",
                "order_id": f"order-{skill_id}-demo",
            }
    raise HTTPException(status_code=404, detail="Skill not found")
