# 🚀 Setup & Installation Guide

Complete step-by-step guide to set up and run the AI Insurance Advisory Platform.

## 📋 Prerequisites

Before starting, ensure you have:
- **Windows 10/11** or **macOS/Linux**
- **Python 3.8 or higher** ([Download Python](https://www.python.org/downloads/))
- **pip** (usually comes with Python)
- **Git** (optional, for cloning)
- **Postman** ([Download Postman](https://www.postman.com/downloads/)) - for API testing
- **Text Editor/IDE** (VS Code, PyCharm, etc.)

## 🔍 Verify Prerequisites

### Check Python Installation
Open Command Prompt (Windows) or Terminal (Mac/Linux) and run:
```bash
python --version
```
Should show Python 3.8 or higher.

### Check pip Installation
```bash
pip --version
```
Should show a version number.

## 📥 Installation Steps

### Step 1: Navigate to Project Directory
```bash
cd "c:\Users\nites\Desktop\ai insurance"
```

### Step 2: Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` at the beginning of your command line.

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

This will install:
- FastAPI (web framework)
- Uvicorn (ASGI server)
- SQLAlchemy (database ORM)
- Pydantic (data validation)

### Step 4: Verify Installation
```bash
pip list
```

You should see all the installed packages listed.

## 🏃 Running the Application

### Option 1: Using Batch Script (Windows)
Double-click `start_server.bat` in the project folder. This will:
1. Check Python installation
2. Install dependencies if needed
3. Start the FastAPI server

### Option 2: Manual Start (All Platforms)

**Windows:**
```bash
uvicorn main:app --reload
```

**macOS/Linux:**
```bash
uvicorn main:app --reload
```

You should see output like:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Will auto-reload on file changes
Launched server process [12345]
Application startup complete
```

### Verify Server is Running
Open your browser and visit: http://localhost:8000/health

You should see: `{"status": "healthy", "service": "AI Insurance Advisory System"}`

## 📚 Accessing API Documentation

Once the server is running:

1. **Swagger UI (Interactive)**: http://localhost:8000/docs
   - Try endpoints directly from the browser
   - See request/response schemas
   - View parameter descriptions

2. **ReDoc (Alternative)**: http://localhost:8000/redoc
   - Clean, readable API documentation
   - Search functionality

## 🔧 Postman Setup

### Import Postman Collection

1. **Download Postman**: https://www.postman.com/downloads/
2. **Open Postman**
3. Click **File** → **Import**
4. Click **Upload Files**
5. Select `Postman_Collection.json` from the project folder
6. Click **Import**

### Test an Endpoint

1. Go to **Collections** → **AI Insurance Advisory Platform**
2. Click on any request (e.g., "Health Check")
3. Click **Send**
4. View the response in the bottom panel

## 📊 Initialize Sample Data

After the server is running, populate the database with sample data:

### Option 1: Using Script
```bash
python init_sample_data.py
```

This will create:
- 4 sample users
- 8 insurance policies
- 8 recommendations
- 2 sample claims

### Option 2: Manual Using Postman

1. Open Postman collection
2. Go to **Users** → **Create User**
3. Click **Send** to create a user
4. Repeat for policies, recommendations, etc.

## 🌐 Testing the API

### With Postman (Recommended)
1. Open Postman
2. Import the collection (see Postman Setup above)
3. Follow the "Suggested Testing Flow" in the collection

### With cURL
```bash
# Check health
curl http://localhost:8000/health

# List users
curl http://localhost:8000/users

# Create a user
curl -X POST "http://localhost:8000/users" \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","name":"Test User","age":30,"health_status":"Good"}'
```

## 📁 Project Files Explained

| File | Purpose |
|------|---------|
| `main.py` | Main FastAPI application with all routes |
| `database.py` | SQLite database configuration |
| `models.py` | SQLAlchemy database models |
| `schemas.py` | Pydantic request/response models |
| `crud.py` | Database CRUD operations |
| `requirements.txt` | Python package dependencies |
| `Postman_Collection.json` | Postman API test collection |
| `init_sample_data.py` | Sample data initialization script |
| `DEMO.html` | Interactive demo presentation |
| `start_server.bat` | Windows batch script to start server |
| `README.md` | Project documentation |
| `SETUP.md` | This setup guide |
| `insurance.db` | SQLite database (created automatically) |

## 🎯 Quick Testing Workflow

### 1. Create Users
In Postman:
- Collections → Users → Create User
- Send 2-3 requests with different user data

### 2. Create Policies
- Collections → Policies → Create Health Policy
- Create additional policies (Life, Auto, Property)

### 3. Create Recommendations
- Collections → Recommendations → Create Recommendation
- Link users to policies

### 4. Get Advisory
- Collections → Advisory → Get User Advisory
- View personalized recommendations

### 5. File Claims
- Collections → Claims → File Claim
- Track claim status

## 🔧 Troubleshooting

### Issue: "Python not found"
**Solution:**
- Install Python from https://www.python.org/downloads/
- Make sure "Add Python to PATH" is checked during installation
- Restart Command Prompt/Terminal

### Issue: "ModuleNotFoundError: No module named 'fastapi'"
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: "Port 8000 already in use"
**Solution:**
Use a different port:
```bash
uvicorn main:app --reload --port 8001
```

### Issue: "Database locked" or SQLite errors
**Solution:**
1. Stop the server (Ctrl+C)
2. Delete `insurance.db` file
3. Restart the server

### Issue: Postman collection import fails
**Solution:**
1. Make sure `Postman_Collection.json` is in the project folder
2. Check file is valid JSON (open with text editor)
3. Try importing again

## 📖 Next Steps

1. **Explore API Documentation**
   - Visit http://localhost:8000/docs
   - Try different endpoints

2. **Review DEMO.html**
   - Open `DEMO.html` in your browser
   - See visual overview of the platform

3. **Test with Postman**
   - Import collection
   - Follow suggested testing flow
   - Try all endpoints

4. **Review Code**
   - Understand project structure
   - Study the API implementation
   - Explore database models

5. **Customize**
   - Add new policies
   - Modify recommendation logic
   - Extend the API

## 🆘 Getting Help

### Check These Resources
1. **README.md** - Full project documentation
2. **DEMO.html** - Interactive demo presentation
3. **FastAPI Docs** - https://fastapi.tiangolo.com
4. **SQLAlchemy Docs** - https://www.sqlalchemy.org

### Common Endpoints to Test

```bash
# Health check
curl http://localhost:8000/health

# API info
curl http://localhost:8000/

# List users
curl http://localhost:8000/users

# Interactive docs
# Open in browser: http://localhost:8000/docs
```

## ✅ Verification Checklist

- [ ] Python 3.8+ installed
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Server starts without errors
- [ ] Can access http://localhost:8000/health
- [ ] Can access http://localhost:8000/docs
- [ ] Postman collection imported
- [ ] Sample data initialized
- [ ] Can create a user via Postman
- [ ] Can list users via Postman
- [ ] DEMO.html opens in browser

## 🎉 You're Ready!

Once all checks pass, you have:
- ✅ Running FastAPI server
- ✅ SQLite database
- ✅ Sample data for testing
- ✅ Postman collection for API testing
- ✅ Interactive demo documentation

**Start exploring the API!**

---

**Need Help?**
- Check the troubleshooting section above
- Review README.md for more details
- Open DEMO.html in browser for tutorial
- Check FastAPI documentation online
