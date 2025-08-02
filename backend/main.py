from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.file_ops import list_project_files, save_file, read_file
from app.vercel import trigger_vercel_deploy
from pydantic import BaseModel
import os

app = FastAPI()

# ➊ CORS middleware MUST be added **immediately after** app creation
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5200", "http://127.0.0.1:5200"],
    allow_methods=["*"],
    allow_headers=["*"],
)
class SaveRequest(BaseModel):
    path: str
    code: str

class DeployRequest(BaseModel):
    vercel_token: str
    project_name: str
    repo_url: str

PROJECT_ROOT = os.path.abspath("..")  # parent folder of backend/

@app.get("/api/files")
def api_files():
    return list_project_files(PROJECT_ROOT)

@app.post("/api/save")
def api_save(req: SaveRequest):
    save_file(PROJECT_ROOT, req.path, req.code)
    return {"status": "ok"}

@app.post("/api/deploy")
def api_deploy(req: DeployRequest):
    deploy_url = trigger_vercel_deploy(
        token=req.vercel_token,
        project=req.project_name,
        repo=req.repo_url,
    )
    return {"deployment_url": deploy_url}


@app.get("/api/read")
def api_read(path: str):
    return {"code": read_file(PROJECT_ROOT, path)}
