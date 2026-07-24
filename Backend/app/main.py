from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import settings
from app.database.database import engine
from app.database.base import Base
from app.middleware.exception_handler import register_exception_handlers
from app.middleware.logging_middleware import RequestLoggingMiddleware
from app.routers import admin

# Auto-create database tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="""
    ## 🏥 Healthcare Clinic Backend API
    **Module 4: Administration & System Integration** (Developed by **Udbhav**)
    
    This enterprise-level backend API provides:
    - 📊 **Admin Dashboard & System Analytics** (`/api/v1/admin/dashboard`)
    - 🛡️ **Zero-Trust Security & Soft-Deletion Architecture** (UUIDs + `is_deleted` flags)
    - 🚨 **Unified Exception Handling Middleware**
    - ⚡ **High-Performance ORM Aggregations**
    """,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc"
)

# 1. Register CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Register Request Logging Middleware
app.add_middleware(RequestLoggingMiddleware)

# 3. Register Global Exception Handlers
register_exception_handlers(app)

# 4. Register Routers
app.include_router(admin.router, prefix=settings.API_V1_STR)


@app.get("/", tags=["Health & Root"])
def root():
    return {
        "status": "online",
        "message": f"Welcome to {settings.PROJECT_NAME}",
        "documentation": "/docs",
        "redoc": "/redoc",
        "module_owner": "Udbhav (Administration & System Integration)"
    }