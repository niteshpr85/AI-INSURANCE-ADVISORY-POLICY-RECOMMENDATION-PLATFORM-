from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# User Schemas
class UserBase(BaseModel):
    email: str
    name: str
    age: int
    health_status: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# Insurance Policy Schemas
class PolicyBase(BaseModel):
    policy_name: str
    policy_type: str
    coverage_amount: float
    monthly_premium: float
    description: str

class PolicyCreate(PolicyBase):
    pass

class Policy(PolicyBase):
    id: int
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

# Recommendation Schemas
class RecommendationBase(BaseModel):
    user_id: int
    policy_id: int
    recommendation_score: float
    reason: str

class RecommendationCreate(RecommendationBase):
    pass

class Recommendation(RecommendationBase):
    id: int
    is_accepted: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

# Claim Schemas
class ClaimBase(BaseModel):
    user_id: int
    policy_id: int
    claim_amount: float
    description: str

class ClaimCreate(ClaimBase):
    pass

class Claim(ClaimBase):
    id: int
    claim_status: str
    created_at: datetime
    
    class Config:
        from_attributes = True

# Advisory Response
class AdvisoryResponse(BaseModel):
    user_id: int
    recommendations: list
    total_coverage: float
    estimated_annual_cost: float
    advice: str
