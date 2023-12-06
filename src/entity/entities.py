import uuid
from typing import List
from uuid import UUID
from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"
    user_id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid1)
    username: Mapped[str] = mapped_column(String())
    password: Mapped[str] = mapped_column(String())
    bio: Mapped[str] = mapped_column(String(), default="")
    posts: Mapped[List["Post"]] = relationship("Post", back_populates="user", cascade="all, delete-orphan")


class Post(Base):
    __tablename__ = "post"
    post_id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid1)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("user.user_id"))
    text: Mapped[str] = mapped_column(String())
    image: Mapped[str] = mapped_column(String())
    posted: Mapped[DateTime] = mapped_column(DateTime())
    user: Mapped["User"] = relationship("User", back_populates="posts")  # 'User' is the class name
