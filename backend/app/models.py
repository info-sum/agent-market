from sqlalchemy import String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.db import Base


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String, nullable=False)
    display_name: Mapped[str | None] = mapped_column(String, nullable=True)


class ConnectionModel(Base):
    __tablename__ = "connections"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    owner_id: Mapped[str] = mapped_column(String, ForeignKey("users.id"), nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    endpoint: Mapped[str] = mapped_column(String, nullable=False)
    scopes: Mapped[str] = mapped_column(String, default="")
    status: Mapped[str] = mapped_column(String, default="active")


class ProductModel(Base):
    __tablename__ = "products"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    type: Mapped[str] = mapped_column(String, nullable=False)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, default="")
    price: Mapped[float] = mapped_column(Float, default=0)


class InstallationModel(Base):
    __tablename__ = "installations"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    owner_id: Mapped[str] = mapped_column(String, ForeignKey("users.id"), nullable=False)
    connection_id: Mapped[str] = mapped_column(String, ForeignKey("connections.id"), nullable=False)
    product_id: Mapped[str] = mapped_column(String, ForeignKey("products.id"), nullable=False)
    status: Mapped[str] = mapped_column(String, default="queued")
    message: Mapped[str] = mapped_column(String, default="")
