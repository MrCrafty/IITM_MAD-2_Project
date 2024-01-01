from website import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from flask_login import UserMixin
from sqlalchemy import DateTime, func
from flask_security import RoleMixin


class Category(db.Model):
    categoryId: Mapped[int] = mapped_column(Integer, autoincrement=True,
                                            unique=True, primary_key=True)
    categoryName: Mapped[str] = mapped_column(String)


class User(db.Model, UserMixin):
    user_id: Mapped[int] = mapped_column(
        Integer, autoincrement=True, nullable=False, primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String)
    cart = mapped_column(String, default="[]")
    created_on = mapped_column(
        DateTime, default=func.now())
    roles = db.relationship("Role")


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
