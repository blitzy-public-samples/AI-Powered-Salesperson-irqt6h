from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False)
    last_login = Column(DateTime, default=datetime.utcnow)

class ChatSession(Base):
    __tablename__ = 'chat_sessions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    start_time = Column(DateTime, default=datetime.utcnow)
    end_time = Column(DateTime)
    status = Column(String, nullable=False)

    user = relationship('User', back_populates='chat_sessions')

class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey('chat_sessions.id'), nullable=False)
    content = Column(Text, nullable=False)
    sent_at = Column(DateTime, default=datetime.utcnow)
    sender_type = Column(String, nullable=False)

    chat_session = relationship('ChatSession', back_populates='messages')

class Quote(Base):
    __tablename__ = 'quotes'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = Column(String, nullable=False)
    total_amount = Column(Float, nullable=False)

    user = relationship('User', back_populates='quotes')
    items = relationship('QuoteItem', back_populates='quote')

class QuoteItem(Base):
    __tablename__ = 'quote_items'

    id = Column(Integer, primary_key=True)
    quote_id = Column(Integer, ForeignKey('quotes.id'), nullable=False)
    sku_id = Column(Integer, ForeignKey('skus.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    total_price = Column(Float, nullable=False)

    quote = relationship('Quote', back_populates='items')
    sku = relationship('SKU', back_populates='quote_items')

class SKU(Base):
    __tablename__ = 'skus'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    base_price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False)

    quote_items = relationship('QuoteItem', back_populates='sku')

# Add these lines to complete the relationships
User.chat_sessions = relationship('ChatSession', back_populates='user')
User.quotes = relationship('Quote', back_populates='user')
ChatSession.messages = relationship('Message', back_populates='chat_session')