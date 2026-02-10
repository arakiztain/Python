from pydantic import BaseModel, Field, model_validator, ValidationError
from typing import Optional, List
from enum import Enum
from datetime import datetime


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: Optional[str] = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=100000.0)

    @model_validator(mode="after")
    def safety_rules(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        if not any(
            m.rank in {Rank.commander, Rank.captain} for m in self.crew
        ):
            raise ValueError("Must have at least one Commander or Captain")

        if self.duration_days > 365:
            experienced_ratio = sum(
                m.years_experience >= 5 for m in self.crew) / len(self.crew)
            if experienced_ratio < 0.5:
                raise ValueError(
                    "Long missions require at least 50%"
                    " experienced crew (5+ years)"
                )

        if any(not m.is_active for m in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 40)

    try:
        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2024-07-20",
            duration_days=900,
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="C001",
                    name="Sarah Connor",
                    rank=Rank.commander,
                    age=45,
                    specialization="Mission Command",
                    years_experience=20,
                ),

                CrewMember(
                    member_id="C002",
                    name="John Smith",
                    rank=Rank.lieutenant,
                    age=38,
                    specialization="Navigation",
                    years_experience=10,
                ),
                CrewMember(
                    member_id="C003",
                    name="Alice Johnson",
                    rank=Rank.officer,
                    age=32,
                    specialization="Engineering",
                    years_experience=7,
                ),
            ],
        )

        print("Valid mission created:")
        print(f"Mission: {valid_mission.mission_name}")
        print(f"ID: {valid_mission.mission_id}")
        print(f"Destination: {valid_mission.destination}")
        print(f"Duration: {valid_mission.duration_days} days")
        print(f"Budget: ${valid_mission.budget_millions}M")
        print(f"Crew size: {len(valid_mission.crew)}")
        print("Crew members:")
        for member in valid_mission.crew:
            print(
                f"- {member.name} ({member.rank.value})"
                f" - {member.specialization}"
            )

    except ValidationError as e:
        print("Validation failed for valid mission:")
        print(e)

    print()
    print("=" * 40)

    try:
        SpaceMission(
            mission_id="M2026_MARS",
            mission_name="Test Flight",
            destination="Moon",
            launch_date=datetime(2025, 1, 1),
            duration_days=30,
            budget_millions=100.0,
            crew=[
                CrewMember(
                    member_id="C010",
                    name="Bob Lee",
                    rank=Rank.officer,
                    age=29,
                    specialization="Science",
                    years_experience=3,
                )
            ],
        )

    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
