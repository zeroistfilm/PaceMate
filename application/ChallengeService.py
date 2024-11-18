from adapter.output.challenge_repository import ChallengeRepository
from application.interfaces import IChallengeService
from domain.dataclasses.challenge_dataclass import Challenge
import uuid
from sqlalchemy.orm import Session
from application.events import ChallengeCreatedEvent

class ChallengeService(IChallengeService):
    def __init__(self, db: Session):
        self.challenge_repository = ChallengeRepository(db)

    def create_challenge(self, challenge_data: dict) -> Challenge:
        challenge = self.challenge_repository.transform_challenge_data(challenge_data)
        self.challenge_repository.add_challenge(challenge)

        # 챌린지 생성 이벤트 발행
        event = ChallengeCreatedEvent(challenge_data=challenge)
        publish_event(event)

        return challenge 