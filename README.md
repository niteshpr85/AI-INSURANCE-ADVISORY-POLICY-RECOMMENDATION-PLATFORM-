# 🛡️ AI Insurance Advisory & Policy Recommendation Platform

An intelligent REST API platform for insurance policy management, personalized recommendations, and claims processing.

## 📋 Overview

This project implements a comprehensive insurance advisory system that:
- Manages user profiles with demographic and health information
- Provides a catalog of insurance policies across multiple categories
- Generates AI-powered policy recommendations based on user profiles
- Delivers personalized insurance advisory
- Handles insurance claims processing and status tracking

## ⚙️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **Backend Framework** | FastAPI |
| **Web Server** | Uvicorn |
| **Database** | SQLite (persist to `insurance.db`) |
| **ORM** | SQLAlchemy 2.0 |
| **Validation** | Pydantic v2 |
| **Testing** | Postman |

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Postman (for API testing and visualization)

### Installation

1. **Navigate to the project directory:**
   ```bash
   cd "c:\Users\nites\Desktop\ai insurance"
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the FastAPI server:**
   ```bash
   uvicorn main:app --reload
   ```

4. **Access the API:**
   - Main API: http://localhost:8000
   - Interactive Docs (Swagger): http://localhost:8000/docs
   - Alternative Docs (ReDoc): http://localhost:8000/redoc

## 📁 Project Structure

```
ai-insurance/
├── main.py                    # FastAPI application and route handlers
├── database.py               # SQLite configuration and session management
├── models.py                 # SQLAlchemy database models
├── schemas.py                # Pydantic request/response schemas
├── crud.py                   # Database CRUD operations
├── requirements.txt          # Python package dependencies
├── Postman_Collection.json   # Postman API test collection
├── DEMO.html                 # Interactive demo presentation
├── README.md                 # This file
└── insurance.db             # SQLite database (auto-created)
```

## 📊 Database Models

### Users Table
Stores user profile information:
```python
{
  "id": int,
  "email": str,  # unique
  "name": str,
  "age": int,
  "health_status": str,  # Good, Fair, Poor
  "created_at": datetime
}
```

### Insurance Policies Table
Available insurance policies:
```python
{
  "id": int,
  "policy_name": str,  # unique
  "policy_type": str,  # Health, Life, Auto, Property
  "coverage_amount": float,
  "monthly_premium": float,
  "description": str,
  "is_active": bool,
  "created_at": datetime
}
```

### Recommendations Table
Policy recommendations for users:
```python
{
  "id": int,
  "user_id": int,  # foreign key
  "policy_id": int,  # foreign key
  "recommendation_score": float,  # 0-100
  "reason": str,
  "is_accepted": bool,
  "created_at": datetime
}
```

### Claims Table
Insurance claims filed by users:
```python
{
  "id": int,
  "user_id": int,  # foreign key
  "policy_id": int,  # foreign key
  "claim_amount": float,
  "claim_status": str,  # Pending, Approved, Rejected
  "description": str,
  "created_at": datetime
}
```

## 🔌 API Endpoints

### Health & Information
- `GET /` - Root endpoint with API information
- `GET /health` - Health check endpoint

### User Management
- `GET /users` - List all users (paginated)
- `GET /users/{user_id}` - Get specific user
- `POST /users` - Create new user
- `PUT /users/{user_id}` - Update user information
- `DELETE /users/{user_id}` - Delete user

### Policy Management
- `GET /policies` - List active policies (paginated)
- `GET /policies/{policy_id}` - Get specific policy
- `GET /policies/type/{policy_type}` - Get policies by type
- `POST /policies` - Create new insurance policy

### Recommendations
- `POST /recommendations` - Create recommendation
- `GET /recommendations/user/{user_id}` - Get user recommendations
- `PUT /recommendations/{recommendation_id}/accept` - Accept recommendation
- `PUT /recommendations/{recommendation_id}/reject` - Reject recommendation

### Advisory
- `GET /advisory/{user_id}` - Get personalized insurance advisory

### Claims Management
- `POST /claims` - File new claim
- `GET /claims/{claim_id}` - Get claim details
- `GET /claims/user/{user_id}` - Get user's claims
- `PUT /claims/{claim_id}/status` - Update claim status

## 📝 API Usage Examples

### 1. Create a User
```bash
curl -X POST "http://localhost:8000/users" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john.doe@example.com",
    "name": "John Doe",
    "age": 35,
    "health_status": "Good"
  }'
```

### 2. Create an Insurance Policy
```bash
curl -X POST "http://localhost:8000/policies" \
  -H "Content-Type: application/json" \
  -d '{
    "policy_name": "Premium Health Plan Plus",
    "policy_type": "Health",
    "coverage_amount": 500000,
    "monthly_premium": 450,
    "description": "Comprehensive health insurance with hospitalization coverage"
  }'
```

### 3. Create a Recommendation
```bash
curl -X POST "http://localhost:8000/recommendations" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1,
    "policy_id": 1,
    "recommendation_score": 85.5,
    "reason": "Based on your age and health status, this plan is ideal"
  }'
```

### 4. Get Personalized Advisory
```bash
curl -X GET "http://localhost:8000/advisory/1"
```

### 5. File an Insurance Claim
```bash
curl -X POST "http://localhost:8000/claims" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1,
    "policy_id": 1,
    "claim_amount": 50000,
    "description": "Hospital treatment for emergency care"
  }'
```

## 🧪 Testing with Postman

### Import the Collection
1. Open Postman
2. Click **Import** in the top left
3. Select **Upload Files** and choose `Postman_Collection.json`
4. The collection will be imported with all endpoints organized

### Recommended Testing Flow
1. **Create Users**: Use "Create User" requests to add 2-3 test users
2. **Create Policies**: Add 4-5 different insurance policies
3. **Generate Recommendations**: Create policy recommendations for users
4. **Get Advisory**: Retrieve personalized advisory for users
5. **Manage Recommendations**: Accept or reject recommendations
6. **File Claims**: Create claims and track their status

## 💡 Key Features

### Intelligent Recommendations
- AI-powered policy matching based on user profiles
- Scoring system (0-100) for recommendation strength
- Personalized reasoning for each recommendation

### Personalized Advisory
Generates contextual insurance advice based on:
- User age group
- Health status
- Coverage diversity
- Policy recommendations

Example advisory:
> "As a young professional, maintaining good health is key. Consider life and disability insurance. Your current recommendations provide good coverage diversity."

### Comprehensive Claims Management
- File claims with detailed descriptions
- Track claim status through workflow
- Support for multiple claim statuses (Pending, Approved, Rejected)

### Multi-Category Insurance Support
- **Health**: Hospital, surgery, diagnostic coverage
- **Life**: Term and whole life insurance protection
- **Auto**: Third-party and comprehensive vehicle coverage
- **Property**: Home, theft, and disaster protection

## 🔧 Troubleshooting

### Port Already in Use
Start the server on a different port:
```bash
uvicorn main:app --reload --port 8001
```

### Reset Database
Delete the database file and restart the application:
```bash
del insurance.db
```

### Missing Dependencies
Install or upgrade all dependencies:
```bash
pip install -r requirements.txt --upgrade
```

### Verify Server Status
Check the health endpoint:
```bash
curl http://localhost:8000/health
```

## 📚 API Documentation

The project includes interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

These provide:
- Complete endpoint documentation
- Request/response schema visualization
- Try-it-out functionality for endpoints
- Parameter descriptions and examples

## 🎯 Demo Presentation

Open `DEMO.html` in a web browser to view:
- Project overview
- Feature demonstrations
- Complete API reference
- Getting started guide
- Code examples
- Testing instructions

## 🚀 Potential Enhancements

### Security & Authentication
- [ ] JWT-based user authentication
- [ ] Role-based access control (Admin, User)
- [ ] API key management

### AI & Analytics
- [ ] Machine learning recommendation engine
- [ ] Advanced insurance need analysis
- [ ] Claims fraud detection
- [ ] Analytics dashboard

### User Experience
- [ ] Web dashboard for users
- [ ] Email notifications
- [ ] SMS alerts for claims
- [ ] Mobile application

### Integrations
- [ ] Payment gateway integration
- [ ] Document upload for claims
- [ ] Third-party insurance APIs
- [ ] Email service integration

### Operations
- [ ] Comprehensive logging
- [ ] Request rate limiting
- [ ] Caching mechanisms
- [ ] Database backup automation

## 📄 License

This project is provided as-is for educational and demonstration purposes.

## 👥 Contributing

This is a demonstration project. For feedback or suggestions, please reach out.

## 📞 Support

For issues or questions about the platform:
1. Check the `DEMO.html` presentation
2. Review the Postman collection for endpoint usage
3. Check FastAPI documentation at https://fastapi.tiangolo.com
4. Review SQLAlchemy documentation at https://www.sqlalchemy.org

## 🎉 Getting Started Checklist

- [ ] Python 3.8+ installed
- [ ] Project files downloaded/cloned
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] FastAPI server started (`uvicorn main:app --reload`)
- [ ] Postman downloaded and imported `Postman_Collection.json`
- [ ] DEMO.html opened in browser
- [ ] Test first endpoint (http://localhost:8000/health)

---

**Version**: 1.0.0  
**Last Updated**: February 2024  
**Powered by**: FastAPI, SQLAlchemy, Pydantic
