from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
from app.api.routes import auth, tasks, users


app = FastAPI(
    title="Cloud-Native DevOps Platform API",
    description="Backend API for the Cloud-Native DevOps Platform",
    version="1.0.0",
)
Instrumentator().instrument(app).expose(app)

@app.get("/health")
def health_check():
    return {"status": "healthy"}
# ---------------------------------------------------------
# CORS Configuration
# ---------------------------------------------------------

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------
# API Routes
# ---------------------------------------------------------

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(tasks.router)


# ---------------------------------------------------------
# Root Endpoint
# ---------------------------------------------------------

@app.get("/")
def root():
    return {
        "message": "Cloud-Native DevOps Platform API",
        "version": "1.0.0",
        "status": "running",
    }


@app.get("/api/health")
def health_check():
    return {"status": "healthy"}