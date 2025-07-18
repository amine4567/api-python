import datetime
from pydantic import BaseModel
from retroachievements.base import BaseRAClient
from retroachievements.models import RAAPIResponse
from retroachievements.utils import convert_date_to_timestamp


class Unlock(RAAPIResponse):
    date: str  # TODO: cast to datetime
    hardcore_mode: int  # TODO: boolean ?
    achievement_id: int
    title: str
    description: str
    badge_name: str
    points: int
    true_ratio: int
    type: str | None  # TODO: not sure of the non-None type
    author: str
    game_title: str
    game_icon: str
    game_id: int
    console_name: str
    cumul_score: int | None = None
    badge_u_r_l: str
    game_u_r_l: str


class UnlocksResponse(BaseModel):
    items: list[Unlock]


def get_user_recent_achievements(self: BaseRAClient, user: str, minutes: int = 60):
    """
    Retrieve a list of a target user's recently unlocked achievements, via their username.
    By default, it fetches achievements unlocked in the last hour.

    Params:
        u: Username to query
        m: Minutes to look back. Defaults to 60.
    """
    response: list[dict] = self._call_api(
        "API_GetUserRecentAchievements.php",
        {"u": user, "m": minutes},
    )
    return UnlocksResponse(items=response).items


def get_achievements_earned_between(
    self: BaseRAClient, user: str, from_date: datetime.date, to_date: datetime.date
):
    """
    Retrieve a list of achievements earned by a given user between two provided dates.
    """
    response: list[dict] = self._call_api(
        "API_GetAchievementsEarnedBetween.php",
        {
            "u": user,
            "f": convert_date_to_timestamp(from_date),
            "t": convert_date_to_timestamp(to_date),
        },
    )
    return UnlocksResponse(items=response).items
