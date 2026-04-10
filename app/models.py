from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, nullable=False, server_default='true')
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    owner_id = Column(Integer, ForeignKey("users.id",ondelete = "cascade"), nullable=False)
    owner = relationship("User", back_populates="posts")
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    posts = relationship("Post", back_populates="owner")
    phone_number = Column(String(15), nullable=False)

    
class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey("users.id", ondelete="cascade"), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="cascade"), primary_key=True)