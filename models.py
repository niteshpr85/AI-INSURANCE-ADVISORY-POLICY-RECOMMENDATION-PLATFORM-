from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Text
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    age = Column(Integer)
    health_status = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class InsurancePolicy(Base):
    __tablename__ = "insurance_policies"
    
    id = Column(Integer, primary_key=True, index=True)
    policy_name = Column(String, unique=True, index=True)
    policy_type = Column(String)  # Health, Life, Auto, Property
    coverage_amount = Column(Float)
    monthly_premium = Column(Float)
    description = Column(Text)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Recommendation(Base):
    __tablename__ = "recommendations"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    policy_id = Column(Integer, index=True)
    recommendation_score = Column(Float)  # 0-100
    reason = Column(Text)
    is_accepted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Claim(Base):
    __tablename__ = "claims"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    policy_id = Column(Integer, index=True)
    claim_amount = Column(Float)
    claim_status = Column(String)  # Pending, Approved, Rejected
    description = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
