from fastapi import APIRouter, HTTPException
from service.ChallengeService import ChallengeService
from domain.dataclasses.challenge_dataclass import Challenge
from pydantic import BaseModel
import uuid

router = APIRouter()
challenge_service = ChallengeService()

class ChallengeCreate(BaseModel):
    title: str
    description: str
    challenge_type: str
    rules: dict

@router.post("/challenges/")
def create_challenge(challenge: ChallengeCreate):
    challenge = challenge_service.create_challenge(
        title=challenge.title,
        description=challenge.description,
        challenge_type=challenge.challenge_type,
        rules=challenge.rules
    )
    return challenge

@router.get("/challenges/{challenge_id}")
def read_challenge(challenge_id: str):
    challenge = challenge_service.get_challenge(uuid.UUID(challenge_id))
    if challenge is None:
        raise HTTPException(status_code=404, detail="Challenge not found")
    return challenge 