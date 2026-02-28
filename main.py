from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from database import engine, get_db, Base
import models
import schemas
import crud

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Insurance Advisory & Policy Recommendation Platform",
    description="An intelligent platform for insurance advisory and policy recommendations",
    version="1.0.0"
)

# Root endpoint - serve dashboard
@app.get("/", response_class=FileResponse)
def read_root():
    return "index.html"

@app.get("/api/info")
def get_api_info():
    return {
        "message": "Welcome to AI Insurance Advisory & Policy Recommendation Platform",
        "version": "1.0.0",
        "endpoints": {
            "users": "/users",
            "policies": "/policies",
            "recommendations": "/recommendations",
            "claims": "/claims",
            "advisory": "/advisory",
            "dashboard": "/"
        }
    }

# ==================== USER ENDPOINTS ====================

@app.get("/users", response_model=list[schemas.User])
def list_users(skip: int = Query(0, ge=0), limit: int = Query(10, le=100), db: Session = Depends(get_db)):
    """Get list of all users"""
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """Get a specific user by ID"""
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """Create a new user"""
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    """Update user information"""
    updated_user = crud.update_user(db, user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Delete a user"""
    user = crud.delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

# ==================== POLICY ENDPOINTS ====================

@app.get("/policies", response_model=list[schemas.Policy])
def list_policies(skip: int = Query(0, ge=0), limit: int = Query(10, le=100), db: Session = Depends(get_db)):
    """Get list of active insurance policies"""
    policies = crud.get_policies(db, skip=skip, limit=limit)
    return policies

@app.get("/policies/type/{policy_type}", response_model=list[schemas.Policy])
def get_policies_by_type(policy_type: str, db: Session = Depends(get_db)):
    """Get policies by type (Health, Life, Auto, Property)"""
    policies = crud.get_policies_by_type(db, policy_type)
    if not policies:
        raise HTTPException(status_code=404, detail=f"No policies found for type: {policy_type}")
    return policies

@app.get("/policies/{policy_id}", response_model=schemas.Policy)
def get_policy(policy_id: int, db: Session = Depends(get_db)):
    """Get a specific policy by ID"""
    policy = crud.get_policy(db, policy_id)
    if not policy:
        raise HTTPException(status_code=404, detail="Policy not found")
    return policy

@app.post("/policies", response_model=schemas.Policy)
def create_policy(policy: schemas.PolicyCreate, db: Session = Depends(get_db)):
    """Create a new insurance policy"""
    existing_policy = crud.get_policy_by_name(db, policy.policy_name)
    if existing_policy:
        raise HTTPException(status_code=400, detail="Policy name already exists")
    return crud.create_policy(db=db, policy=policy)

# ==================== RECOMMENDATION ENDPOINTS ====================

@app.post("/recommendations", response_model=schemas.Recommendation)
def create_recommendation(recommendation: schemas.RecommendationCreate, db: Session = Depends(get_db)):
    """Create a policy recommendation for a user"""
    # Verify user exists
    user = crud.get_user(db, recommendation.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Verify policy exists
    policy = crud.get_policy(db, recommendation.policy_id)
    if not policy:
        raise HTTPException(status_code=404, detail="Policy not found")
    
    return crud.create_recommendation(db=db, recommendation=recommendation)

@app.get("/recommendations/user/{user_id}", response_model=list[schemas.Recommendation])
def get_user_recommendations(user_id: int, db: Session = Depends(get_db)):
    """Get all recommendations for a specific user"""
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    recommendations = crud.get_recommendations_for_user(db, user_id)
    return recommendations

@app.put("/recommendations/{recommendation_id}/accept")
def accept_recommendation(recommendation_id: int, db: Session = Depends(get_db)):
    """Accept a recommendation"""
    recommendation = crud.update_recommendation_status(db, recommendation_id, True)
    if not recommendation:
        raise HTTPException(status_code=404, detail="Recommendation not found")
    return {"message": "Recommendation accepted", "recommendation": recommendation}

@app.put("/recommendations/{recommendation_id}/reject")
def reject_recommendation(recommendation_id: int, db: Session = Depends(get_db)):
    """Reject a recommendation"""
    recommendation = crud.update_recommendation_status(db, recommendation_id, False)
    if not recommendation:
        raise HTTPException(status_code=404, detail="Recommendation not found")
    return {"message": "Recommendation rejected", "recommendation": recommendation}

# ==================== ADVISORY ENDPOINT ====================

@app.get("/advisory/{user_id}")
def get_advisory(user_id: int, db: Session = Depends(get_db)):
    """Get AI-powered insurance advisory for a user"""
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Get recommendations for user
    recommendations = crud.get_recommendations_for_user(db, user_id)
    
    # Calculate totals
    total_coverage = sum(db.query(models.InsurancePolicy).filter(
        models.InsurancePolicy.id == rec.policy_id
    ).first().coverage_amount for rec in recommendations if db.query(models.InsurancePolicy).filter(
        models.InsurancePolicy.id == rec.policy_id
    ).first())
    
    estimated_annual_cost = sum(db.query(models.InsurancePolicy).filter(
        models.InsurancePolicy.id == rec.policy_id
    ).first().monthly_premium * 12 for rec in recommendations if db.query(models.InsurancePolicy).filter(
        models.InsurancePolicy.id == rec.policy_id
    ).first())
    
    # Generate advice based on user profile
    advice = generate_advisory_advice(user, recommendations)
    
    return {
        "user_id": user_id,
        "user_name": user.name,
        "recommendations": [{"policy_id": rec.policy_id, "score": rec.recommendation_score, "reason": rec.reason} for rec in recommendations],
        "total_coverage": total_coverage,
        "estimated_annual_cost": estimated_annual_cost,
        "advice": advice
    }

def generate_advisory_advice(user: models.User, recommendations: list) -> str:
    """Generate personalized insurance advice based on user profile"""
    if user.age < 30:
        base_advice = "As a young professional, "
    elif user.age < 50:
        base_advice = "As a middle-aged individual, "
    else:
        base_advice = "As a senior, "
    
    if user.health_status == "Good":
        health_advice = "maintaining good health is key. Consider life and disability insurance."
    elif user.health_status == "Fair":
        health_advice = "focus on comprehensive health and life insurance coverage."
    else:
        health_advice = "prioritize health insurance and comprehensive coverage."
    
    if len(recommendations) == 0:
        coverage_advice = "We recommend reviewing available policies to ensure adequate protection."
    elif len(recommendations) < 3:
        coverage_advice = "Consider diversifying your coverage with additional policies."
    else:
        coverage_advice = "Your current recommendations provide good coverage diversity."
    
    return f"{base_advice}{health_advice} {coverage_advice}"

# ==================== CLAIMS ENDPOINTS ====================

@app.post("/claims", response_model=schemas.Claim)
def create_claim(claim: schemas.ClaimCreate, db: Session = Depends(get_db)):
    """File an insurance claim"""
    # Verify user exists
    user = crud.get_user(db, claim.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Verify policy exists
    policy = crud.get_policy(db, claim.policy_id)
    if not policy:
        raise HTTPException(status_code=404, detail="Policy not found")
    
    return crud.create_claim(db=db, claim=claim)

@app.get("/claims/{claim_id}", response_model=schemas.Claim)
def get_claim(claim_id: int, db: Session = Depends(get_db)):
    """Get claim details"""
    claim = crud.get_claim(db, claim_id)
    if not claim:
        raise HTTPException(status_code=404, detail="Claim not found")
    return claim

@app.get("/claims/user/{user_id}", response_model=list[schemas.Claim])
def get_user_claims(user_id: int, db: Session = Depends(get_db)):
    """Get all claims for a user"""
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    claims = crud.get_claims_for_user(db, user_id)
    return claims

@app.put("/claims/{claim_id}/status")
def update_claim_status(claim_id: int, status: str = Query(..., description="Pending, Approved, or Rejected"), db: Session = Depends(get_db)):
    """Update claim status"""
    if status not in ["Pending", "Approved", "Rejected"]:
        raise HTTPException(status_code=400, detail="Invalid status. Use: Pending, Approved, or Rejected")
    
    claim = crud.update_claim_status(db, claim_id, status)
    if not claim:
        raise HTTPException(status_code=404, detail="Claim not found")
    return {"message": f"Claim status updated to {status}", "claim": claim}

# ==================== HEALTH CHECK ====================

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "AI Insurance Advisory System"}
