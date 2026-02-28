"""
Direct database population script
"""
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import User, InsurancePolicy, Recommendation, Claim
import models

# Create tables
models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Clear existing data
db.query(Claim).delete()
db.query(Recommendation).delete()
db.query(InsurancePolicy).delete()
db.query(User).delete()
db.commit()

print("Creating sample users...")
users = [
    User(email="john@example.com", name="John Doe", age=35, health_status="Good"),
    User(email="jane@example.com", name="Jane Smith", age=42, health_status="Fair"),
    User(email="robert@example.com", name="Robert Wilson", age=55, health_status="Good"),
    User(email="sarah@example.com", name="Sarah Johnson", age=28, health_status="Excellent"),
]
for user in users:
    db.add(user)
db.commit()
print(f"✓ Created {len(users)} users")

print("\nCreating sample policies...")
policies = [
    InsurancePolicy(policy_name="Premium Health Plan", policy_type="Health", 
                   coverage_amount=500000, monthly_premium=450, 
                   description="Comprehensive health insurance"),
    InsurancePolicy(policy_name="Health Basic", policy_type="Health", 
                   coverage_amount=250000, monthly_premium=200, 
                   description="Basic health insurance"),
    InsurancePolicy(policy_name="Life Secure", policy_type="Life", 
                   coverage_amount=1000000, monthly_premium=300, 
                   description="Term life insurance"),
    InsurancePolicy(policy_name="Life Plus", policy_type="Life", 
                   coverage_amount=1500000, monthly_premium=400, 
                   description="Enhanced life insurance"),
    InsurancePolicy(policy_name="Auto Protect", policy_type="Auto", 
                   coverage_amount=300000, monthly_premium=150, 
                   description="Comprehensive auto insurance"),
    InsurancePolicy(policy_name="Auto Basic", policy_type="Auto", 
                   coverage_amount=150000, monthly_premium=80, 
                   description="Third-party auto insurance"),
    InsurancePolicy(policy_name="Home Guardian", policy_type="Property", 
                   coverage_amount=2000000, monthly_premium=200, 
                   description="Property insurance"),
    InsurancePolicy(policy_name="Home Secure", policy_type="Property", 
                   coverage_amount=1000000, monthly_premium=120, 
                   description="Basic property insurance"),
]
for policy in policies:
    db.add(policy)
db.commit()
print(f"✓ Created {len(policies)} policies")

print("\nCreating sample recommendations...")
recommendations = [
    Recommendation(user_id=1, policy_id=1, recommendation_score=85.5, 
                  reason="Based on age and health, this plan is ideal"),
    Recommendation(user_id=1, policy_id=3, recommendation_score=90.0, 
                  reason="Life insurance protects your family"),
    Recommendation(user_id=2, policy_id=2, recommendation_score=78.0, 
                  reason="Cost-effective health coverage"),
    Recommendation(user_id=2, policy_id=7, recommendation_score=88.0, 
                  reason="Important for home protection"),
    Recommendation(user_id=3, policy_id=1, recommendation_score=92.0, 
                  reason="Premium coverage for your age"),
    Recommendation(user_id=3, policy_id=4, recommendation_score=88.0, 
                  reason="Maximum family security"),
    Recommendation(user_id=4, policy_id=2, recommendation_score=80.0, 
                  reason="Health insurance essential"),
    Recommendation(user_id=4, policy_id=5, recommendation_score=85.0, 
                  reason="Comprehensive auto protection"),
]
for rec in recommendations:
    db.add(rec)
db.commit()
print(f"✓ Created {len(recommendations)} recommendations")

print("\nCreating sample claims...")
claims = [
    Claim(user_id=1, policy_id=1, claim_amount=50000, claim_status="Pending",
         description="Hospital treatment"),
    Claim(user_id=2, policy_id=2, claim_amount=25000, claim_status="Pending",
         description="Medical procedure"),
]
for claim in claims:
    db.add(claim)
db.commit()
print(f"✓ Created {len(claims)} claims")

db.close()

print("\n" + "="*50)
print("✅ Sample data loaded successfully!")
print("="*50)
print("\n📊 Data Summary:")
print("   • 4 Users")
print("   • 8 Insurance Policies")
print("   • 8 Recommendations")
print("   • 2 Claims")
print("\nRefresh your dashboard to see the data!")
