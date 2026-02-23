from pydantic import BaseModel, EmailStr, Field


class UserRegister(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    display_name: str | None = None


class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)


class UserOut(BaseModel):
    id: str
    email: EmailStr
    display_name: str | None = None


class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"


class AuthResponse(BaseModel):
    user: UserOut
    token: TokenOut
