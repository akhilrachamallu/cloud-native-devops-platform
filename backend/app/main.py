from fastapi import FastAPI

from app.api.routes import auth, tasks, users

app = FastAPI(
    title="Cloud-Native DevOps Platform API",
    description="Backend API for the Cloud-Native DevOps Platform",
    version="1.0.0",
)

app.include_router(users.router)
app.include_router(tasks.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {
        "message": "Cloud-Native DevOps Platform API",
        "version": "1.0.0",
        "status": "running",
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
    }