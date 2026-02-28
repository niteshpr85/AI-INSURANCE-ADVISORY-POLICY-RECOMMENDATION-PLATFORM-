from sqlalchemy.orm import Session
import models
import schemas

# User CRUD Operations
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: schemas.UserCreate):
    db_user = get_user(db, user_id)
    if db_user:
        for key, value in user.model_dump().items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

# Policy CRUD Operations
def get_policy(db: Session, policy_id: int):
    return db.query(models.InsurancePolicy).filter(models.InsurancePolicy.id == policy_id).first()

def get_policy_by_name(db: Session, policy_name: str):
    return db.query(models.InsurancePolicy).filter(models.InsurancePolicy.policy_name == policy_name).first()

def get_policies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.InsurancePolicy).filter(models.InsurancePolicy.is_active == True).offset(skip).limit(limit).all()

def get_all_policies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.InsurancePolicy).offset(skip).limit(limit).all()

def create_policy(db: Session, policy: schemas.PolicyCreate):
    db_policy = models.InsurancePolicy(**policy.model_dump())
    db.add(db_policy)
    db.commit()
    db.refresh(db_policy)
    return db_policy

def get_policies_by_type(db: Session, policy_type: str):
    return db.query(models.InsurancePolicy).filter(
        models.InsurancePolicy.policy_type == policy_type,
        models.InsurancePolicy.is_active == True
    ).all()

# Recommendation CRUD Operations
def create_recommendation(db: Session, recommendation: schemas.RecommendationCreate):
    db_recommendation = models.Recommendation(**recommendation.model_dump())
    db.add(db_recommendation)
    db.commit()
    db.refresh(db_recommendation)
    return db_recommendation

def get_recommendations_for_user(db: Session, user_id: int):
    return db.query(models.Recommendation).filter(models.Recommendation.user_id == user_id).all()

def update_recommendation_status(db: Session, recommendation_id: int, is_accepted: bool):
    db_rec = db.query(models.Recommendation).filter(models.Recommendation.id == recommendation_id).first()
    if db_rec:
        db_rec.is_accepted = is_accepted
        db.commit()
        db.refresh(db_rec)
    return db_rec

# Claim CRUD Operations
def create_claim(db: Session, claim: schemas.ClaimCreate):
    db_claim = models.Claim(**claim.model_dump(), claim_status="Pending")
    db.add(db_claim)
    db.commit()
    db.refresh(db_claim)
    return db_claim

def get_claim(db: Session, claim_id: int):
    return db.query(models.Claim).filter(models.Claim.id == claim_id).first()

def get_claims_for_user(db: Session, user_id: int):
    return db.query(models.Claim).filter(models.Claim.user_id == user_id).all()

def update_claim_status(db: Session, claim_id: int, status: str):
    db_claim = get_claim(db, claim_id)
    if db_claim:
        db_claim.claim_status = status
        db.commit()
        db.refresh(db_claim)
    return db_claim
