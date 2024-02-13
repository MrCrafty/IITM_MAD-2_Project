from website import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from flask_login import UserMixin
from sqlalchemy import DateTime, func, ForeignKey


class User(db.Model, UserMixin):
    __tablename__ = "user"
    user_id: Mapped[int] = mapped_column(
        Integer, autoincrement=True, nullable=False, primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String)
    created_on: Mapped[DateTime] = mapped_column(
        DateTime, default=func.now())
    roles: Mapped[str] = mapped_column(String)
    issued_books: Mapped[str] = mapped_column(String)


class Section(db.Model):
    __tablename__ = "section"
    section_id: Mapped[int] = mapped_column(
        Integer, autoincrement=True, nullable=False, primary_key=True)
    section_name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    created_on: Mapped[DateTime] = mapped_column(DateTime, default=func.now())


class Book(db.Model):
    __tablename__ = "book"
    book_id: Mapped[int] = mapped_column(
        Integer, autoincrement=True, nullable=False, primary_key=True)
    book_name: Mapped[str] = mapped_column(String)
    section_id: Mapped[int] = mapped_column(ForeignKey("section.section_id"))
    content: Mapped[str] = mapped_column(String)
    author: Mapped[str] = mapped_column(String)
    created_on: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    issued_by: Mapped[int] = mapped_column(Integer)
    issue_date: Mapped[str] = mapped_column(String)


class Requests(db.Model):
    __tablename__ = "request"
    request_id: Mapped[int] = mapped_column(
        Integer, autoincrement=True, nullable=False, primary_key=True)
    request_by: Mapped[int] = mapped_column(ForeignKey("user.user_id"))
