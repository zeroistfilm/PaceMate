from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from application.UserService import UserService
from application.ClubService import ClubService
from application.EventService import EventService
from application.NotificationService import NotificationService
from application.WorkoutService import WorkoutService
from application.ChallengeService import ChallengeService
from adapter.input.user_controller import router as user_router
from adapter.input.club_controller import router as club_router
from adapter.input.event_controller import router as event_router
from adapter.input.notification_controller import router as notification_router
from adapter.input.workout_controller import router as workout_router
from adapter.input.challenge_controller import router as challenge_router

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 데이터베이스 설정
DATABASE_URL = "sqlite:///./test.db"  # SQLite 데이터베이스 URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 서비스 인스턴스 생성
def get_user_service(db: Session = Depends(SessionLocal)) -> UserService:
    return UserService(db)

def get_club_service(db: Session = Depends(SessionLocal)) -> ClubService:
    return ClubService(db)

def get_event_service(db: Session = Depends(SessionLocal)) -> EventService:
    return EventService(db)

def get_notification_service(db: Session = Depends(SessionLocal)) -> NotificationService:
    return NotificationService(db)

def get_workout_service(db: Session = Depends(SessionLocal)) -> WorkoutService:
    return WorkoutService(db)

def get_challenge_service(db: Session = Depends(SessionLocal)) -> ChallengeService:
    return ChallengeService(db)

# 라우터 등록
app.include_router(user_router, tags=["users"], dependencies=[Depends(get_user_service)])
app.include_router(club_router, tags=["clubs"], dependencies=[Depends(get_club_service)])
app.include_router(event_router, tags=["events"], dependencies=[Depends(get_event_service)])
app.include_router(notification_router, tags=["notifications"], dependencies=[Depends(get_notification_service)])
app.include_router(workout_router, tags=["workouts"], dependencies=[Depends(get_workout_service)])
app.include_router(challenge_router, tags=["challenges"], dependencies=[Depends(get_challenge_service)])

# 데이터베이스 테이블 생성
def init_db():
    db = SessionLocal()
    # 테이블 생성 로직
    db.close()

# 데이터베이스 초기화 호출
init_db() 