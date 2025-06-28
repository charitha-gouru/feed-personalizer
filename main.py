print("Running main.py")
import json
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from ranker import score_and_rank
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all for local testing
    allow_methods=["*"],
    allow_headers=["*"],
)

class Post(BaseModel):
    post_id: str
    author_id: str
    tags: List[str]
    content_type: str
    karma: int
    created_at: str

class UserProfile(BaseModel):
    branches_of_interest: List[str]
    tags_followed: List[str]
    buddies: List[str]
    active_hours: List[str]

class RankRequest(BaseModel):
    user_id: str
    posts: List[Post]
    user_profile: UserProfile

@app.post("/rank-feed")
async def rank_feed(request: RankRequest):
    ranked = score_and_rank(request.posts, request.user_profile)
    return {
        "user_id": request.user_id,
        "ranked_posts": ranked,
        "status": "ranked"
    }

@app.get("/")
async def root():
    return {"message": "API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    with open("config.json") as f:
        config = json.load(f)
    return {"model_version": config["model_version"]}
