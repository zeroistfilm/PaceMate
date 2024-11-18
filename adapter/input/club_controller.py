from fastapi import APIRouter, HTTPException
from service.ClubService import ClubService
from domain.dataclasses.club_dataclass import Club
from pydantic import BaseModel
import uuid

router = APIRouter()
club_service = ClubService()

class ClubCreate(BaseModel):
    name: str
    description: str
    club_type: str
    visibility: str
    location: str

@router.post("/clubs/")
def create_club(club: ClubCreate):
    club = club_service.create_club(
        name=club.name,
        description=club.description,
        club_type=club.club_type,
        visibility=club.visibility,
        location=club.location
    )
    return club

@router.get("/clubs/{club_id}")
def read_club(club_id: str):
    club = club_service.get_club(uuid.UUID(club_id))
    if club is None:
        raise HTTPException(status_code=404, detail="Club not found")
    return club

@router.post("/clubs/{club_id}/join/{user_id}")
def join_club(club_id: str, user_id: str, role: str = "MEMBER"):
    success = club_service.add_member(uuid.UUID(club_id), uuid.UUID(user_id), role)
    if not success:
        raise HTTPException(status_code=404, detail="Club not found or user already a member")
    return {"message": "User successfully joined the club"} 