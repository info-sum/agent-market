from uuid import uuid4
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy import select
from app.db import SessionLocal
from app.models import UserModel
from app.core.security import hash_password, verify_password, create_access_token
from app.deps import get_current_user
from app.schemas.auth import UserRegister, UserLogin, UserOut, TokenOut, AuthResponse

router = APIRouter(tags=["auth"])


@router.post("/auth/register", response_model=AuthResponse)
def register(payload: UserRegister):
    with SessionLocal() as db:
        exists = db.scalar(select(UserModel).where(UserModel.email == payload.email))
        if exists:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="email already exists")

        user = UserModel(
            id=str(uuid4()),
            email=payload.email,
            password_hash=hash_password(payload.password),
            display_name=payload.display_name,
        )
        db.add(user)
        db.commit()

        token = create_access_token(user.id)
        return AuthResponse(
            user=UserOut(id=user.id, email=user.email, display_name=user.display_name),
            token=TokenOut(access_token=token),
        )


@router.post("/auth/login", response_model=AuthResponse)
def login(payload: UserLogin):
    with SessionLocal() as db:
        user = db.scalar(select(UserModel).where(UserModel.email == payload.email))
        if not user or not verify_password(payload.password, user.password_hash):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid credentials")

        token = create_access_token(user.id)
        return AuthResponse(
            user=UserOut(id=user.id, email=user.email, display_name=user.display_name),
            token=TokenOut(access_token=token),
        )


@router.get("/auth/me", response_model=UserOut)
def me(current_user: UserModel = Depends(get_current_user)):
    return UserOut(id=current_user.id, email=current_user.email, display_name=current_user.display_name)
