from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from adapter.input.user_controller import router as user_router
from adapter.input.workout_controller import router as workout_router
from adapter.input.challenge_controller import router as challenge_router
from adapter.input.club_controller import router as club_router
from adapter.input.event_controller import router as event_router
from adapter.input.notification_controller import router as notification_router
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from adapter.output.user_repository import UserRepository
from adapter.output.workout_repository import WorkoutRepository
from adapter.output.challenge_repository import ChallengeRepository
from adapter.output.club_repository import ClubRepository
from adapter.output.event_repository import EventRepository
from adapter.output.notification_repository import NotificationRepository

app = FastAPI()

# CORS 설정 (필요한 경우)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 출처 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(user_router)
app.include_router(workout_router)
app.include_router(challenge_router)
app.include_router(club_router)
app.include_router(event_router)
app.include_router(notification_router)

# 데이터베이스 설정
DATABASE_URL = "sqlite:///./test.db"  # SQLite 데이터베이스 URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 데이터베이스 테이블 생성
def init_db():
    db = SessionLocal()
    user_repo = UserRepository(db)
    workout_repo = WorkoutRepository(db)
    challenge_repo = ChallengeRepository(db)
    club_repo = ClubRepository(db)
    event_repo = EventRepository(db)
    notification_repo = NotificationRepository(db)

    user_repo.create_table()
    workout_repo.create_table()
    challenge_repo.create_table()
    club_repo.create_table()
    event_repo.create_table()
    notification_repo.create_table()

    db.close()

# 데이터베이스 초기화 호출
init_db() 