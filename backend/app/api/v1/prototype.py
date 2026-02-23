from uuid import uuid4
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from app.db import SessionLocal
from app.models import ConnectionModel, ProductModel, InstallationModel, UserModel
from app.schemas.prototype import (
    ConnectionCreate,
    Connection,
    ProductCreate,
    Product,
    InstallationCreate,
    Installation,
)
from app.deps import get_current_user

router = APIRouter(tags=["prototype"])


def _scopes_to_str(scopes: list[str]) -> str:
    return ",".join(scopes)


def _scopes_to_list(scopes: str) -> list[str]:
    if not scopes:
        return []
    return [s for s in scopes.split(",") if s]


@router.get("/connections", response_model=list[Connection])
def list_connections(current_user: UserModel = Depends(get_current_user)):
    with SessionLocal() as db:
        rows = db.scalars(select(ConnectionModel).where(ConnectionModel.owner_id == current_user.id)).all()
        return [
            Connection(id=r.id, name=r.name, endpoint=r.endpoint, scopes=_scopes_to_list(r.scopes), status=r.status)
            for r in rows
        ]


@router.post("/connections", response_model=Connection)
def create_connection(payload: ConnectionCreate, current_user: UserModel = Depends(get_current_user)):
    with SessionLocal() as db:
        row = ConnectionModel(
            id=str(uuid4()),
            owner_id=current_user.id,
            name=payload.name,
            endpoint=payload.endpoint,
            scopes=_scopes_to_str(payload.scopes),
            status="active",
        )
        db.add(row)
        db.commit()
        return Connection(id=row.id, name=row.name, endpoint=row.endpoint, scopes=payload.scopes, status=row.status)


@router.get("/products", response_model=list[Product])
def list_products():
    with SessionLocal() as db:
        rows = db.scalars(select(ProductModel)).all()
        return [Product(id=r.id, type=r.type, title=r.title, description=r.description, price=r.price) for r in rows]


@router.post("/products", response_model=Product)
def create_product(payload: ProductCreate, current_user: UserModel = Depends(get_current_user)):
    _ = current_user
    with SessionLocal() as db:
        row = ProductModel(
            id=str(uuid4()),
            type=payload.type,
            title=payload.title,
            description=payload.description,
            price=payload.price,
        )
        db.add(row)
        db.commit()
        return Product(id=row.id, type=row.type, title=row.title, description=row.description, price=row.price)


@router.get("/installations", response_model=list[Installation])
def list_installations(current_user: UserModel = Depends(get_current_user)):
    with SessionLocal() as db:
        rows = db.scalars(select(InstallationModel).where(InstallationModel.owner_id == current_user.id)).all()
        return [
            Installation(
                id=r.id,
                connection_id=r.connection_id,
                product_id=r.product_id,
                status=r.status,
                message=r.message,
            )
            for r in rows
        ]


@router.post("/installations", response_model=Installation)
def create_installation(payload: InstallationCreate, current_user: UserModel = Depends(get_current_user)):
    with SessionLocal() as db:
        c = db.scalar(
            select(ConnectionModel).where(
                ConnectionModel.id == payload.connection_id,
                ConnectionModel.owner_id == current_user.id,
            )
        )
        p = db.get(ProductModel, payload.product_id)
        if not c or not p:
            raise HTTPException(status_code=404, detail="connection or product not found")

        row = InstallationModel(
            id=str(uuid4()),
            owner_id=current_user.id,
            connection_id=payload.connection_id,
            product_id=payload.product_id,
            status="installed",
            message="prototype install success",
        )
        db.add(row)
        db.commit()
        return Installation(
            id=row.id,
            connection_id=row.connection_id,
            product_id=row.product_id,
            status=row.status,
            message=row.message,
        )
