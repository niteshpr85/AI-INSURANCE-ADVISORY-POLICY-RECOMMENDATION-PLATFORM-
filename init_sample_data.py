"""
Sample Data Initialization Script
Populate the database with sample data for testing
Run this script after starting the FastAPI server
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def create_sample_users():
    """Create sample users"""
    users_data = [
        {
            "email": "john.doe@example.com",
            "name": "John Doe",
            "age": 35,
            "health_status": "Good"
        },
        {
            "email": "jane.smith@example.com",
            "name": "Jane Smith",
            "age": 42,
            "health_status": "Fair"
        },
        {
            "email": "robert.wilson@example.com",
            "name": "Robert Wilson",
            "age": 55,
            "health_status": "Good"
        },
        {
            "email": "sarah.johnson@example.com",
            "name": "Sarah Johnson",
            "age": 28,
            "health_status": "Excellent"
        }
    ]
    
    print("\n📝 Creating sample users...")
    for user in users_data:
        response = requests.post(f"{BASE_URL}/users", json=user)
        if response.status_code == 200:
            print(f"✓ Created user: {user['name']}")
        else:
            print(f"✗ Failed to create user: {user['name']}")

def create_sample_policies():
    """Create sample insurance policies"""
    policies_data = [
        {
            "policy_name": "Premium Health Plan Plus",
            "policy_type": "Health",
            "coverage_amount": 500000,
            "monthly_premium": 450,
            "description": "Comprehensive health insurance with hospitalization, surgery, and diagnostic coverage"
        },
        {
            "policy_name": "Health Basic",
            "policy_type": "Health",
            "coverage_amount": 250000,
            "monthly_premium": 200,
            "description": "Basic health insurance for essential medical care"
        },
        {
            "policy_name": "Life Secure Plan",
            "policy_type": "Life",
            "coverage_amount": 1000000,
            "monthly_premium": 300,
            "description": "Term life insurance providing financial security to family for 20 years"
        },
        {
            "policy_name": "Life Protect Plus",
            "policy_type": "Life",
            "coverage_amount": 1500000,
            "monthly_premium": 400,
            "description": "Enhanced life insurance with additional benefits"
        },
        {
            "policy_name": "Auto Protect Plus",
            "policy_type": "Auto",
            "coverage_amount": 300000,
            "monthly_premium": 150,
            "description": "Comprehensive auto insurance covering third-party and own damage"
        },
        {
            "policy_name": "Auto Basic",
            "policy_type": "Auto",
            "coverage_amount": 150000,
            "monthly_premium": 80,
            "description": "Third-party liability auto insurance"
        },
        {
            "policy_name": "Home Guardian",
            "policy_type": "Property",
            "coverage_amount": 2000000,
            "monthly_premium": 200,
            "description": "Property insurance covering structural damage, theft, and natural disasters"
        },
        {
            "policy_name": "Home Secure",
            "policy_type": "Property",
            "coverage_amount": 1000000,
            "monthly_premium": 120,
            "description": "Basic property insurance for home protection"
        }
    ]
    
    print("\n📋 Creating sample insurance policies...")
    for policy in policies_data:
        response = requests.post(f"{BASE_URL}/policies", json=policy)
        if response.status_code == 200:
            print(f"✓ Created policy: {policy['policy_name']}")
        else:
            print(f"✗ Failed to create policy: {policy['policy_name']}")

def create_sample_recommendations():
    """Create sample recommendations"""
    recommendations_data = [
        {
            "user_id": 1,
            "policy_id": 1,
            "recommendation_score": 85.5,
            "reason": "Based on age and health status, this comprehensive health plan is ideal for you"
        },
        {
            "user_id": 1,
            "policy_id": 3,
            "recommendation_score": 90.0,
            "reason": "Life insurance is essential for your age group to protect family's financial future"
        },
        {
            "user_id": 2,
            "policy_id": 2,
            "recommendation_score": 78.0,
            "reason": "Basic health plan covers essential medical needs at lower cost"
        },
        {
            "user_id": 2,
            "policy_id": 7,
            "recommendation_score": 88.0,
            "reason": "Home protection is important given current property values"
        },
        {
            "user_id": 3,
            "policy_id": 1,
            "recommendation_score": 92.0,
            "reason": "Premium health coverage recommended for your age group"
        },
        {
            "user_id": 3,
            "policy_id": 4,
            "recommendation_score": 88.0,
            "reason": "Enhanced life protection for maximum family security"
        },
        {
            "user_id": 4,
            "policy_id": 2,
            "recommendation_score": 80.0,
            "reason": "Health insurance essential for young professionals"
        },
        {
            "user_id": 4,
            "policy_id": 5,
            "recommendation_score": 85.0,
            "reason": "Comprehensive auto protection recommended for safety"
        }
    ]
    
    print("\n💡 Creating sample recommendations...")
    for rec in recommendations_data:
        response = requests.post(f"{BASE_URL}/recommendations", json=rec)
        if response.status_code == 200:
            print(f"✓ Created recommendation for user {rec['user_id']} -> policy {rec['policy_id']}")
        else:
            print(f"✗ Failed to create recommendation")

def create_sample_claims():
    """Create sample claims"""
    claims_data = [
        {
            "user_id": 1,
            "policy_id": 1,
            "claim_amount": 50000,
            "description": "Hospital treatment for emergency care"
        },
        {
            "user_id": 2,
            "policy_id": 2,
            "claim_amount": 25000,
            "description": "Surgical procedure and hospitalization"
        }
    ]
    
    print("\n🚨 Creating sample claims...")
    for claim in claims_data:
        response = requests.post(f"{BASE_URL}/claims", json=claim)
        if response.status_code == 200:
            print(f"✓ Created claim for user {claim['user_id']} - Amount: ${claim['claim_amount']}")
        else:
            print(f"✗ Failed to create claim")

def main():
    """Initialize sample data"""
    print("=" * 60)
    print("🛡️  AI Insurance Platform - Sample Data Initialization")
    print("=" * 60)
    
    try:
        # Check if server is running
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code != 200:
            print("❌ Error: FastAPI server is not running!")
            print("Please start the server with: uvicorn main:app --reload")
            return
        
        print("✓ Connected to server successfully")
        
        # Create sample data
        create_sample_users()
        create_sample_policies()
        create_sample_recommendations()
        create_sample_claims()
        
        print("\n" + "=" * 60)
        print("✅ Sample data initialization complete!")
        print("=" * 60)
        print("\n📊 Sample data created:")
        print("   • 4 Users")
        print("   • 8 Insurance Policies")
        print("   • 8 Recommendations")
        print("   • 2 Claims")
        print("\nYou can now test the API with Postman or curl!")
        print("\nOpen DEMO.html in a browser for more information.")
        
    except requests.exceptions.ConnectionError:
        print("❌ Error: Cannot connect to the FastAPI server!")
        print("Make sure the server is running: uvicorn main:app --reload")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()
