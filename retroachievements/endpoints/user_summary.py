from retroachievements.base import BaseRAClient
from retroachievements.models import RAAPIResponse, custom_to_pascal


class LastActivityResponse(RAAPIResponse):
    class Config:
        def alias_generator(snake: str):
            return custom_to_pascal(
                snake,
                dont_alias=["timestamp", "lastupdate", "activitytype", "data", "data2"],
            )

    id: int
    timestamp: str | None  # TODO: not sure of the not None type
    lastupdate: str | None  # TODO: not sure of the not None type
    activitytype: str | None  # TODO: not sure of the not None type
    user: str
    data: str | None  # TODO: not sure of the not None type
    data2: str | None  # TODO: not sure of the not None type


class LastGameResponse(RAAPIResponse):
    id: int
    title: str
    console_id: int
    console_name: str
    forum_topic_id: int
    flags: int
    image_icon: str
    image_title: str
    image_ingame: str
    image_box_art: str
    publisher: str
    developer: str
    genre: str
    released: str
    is_final: int  # TODO: boolean ?


class RecentAchievementsResponse(RAAPIResponse):
    id: int
    game_id: int
    game_title: str
    title: str
    description: str
    points: int
    type: str | None  # TODO: not sure of the not None type
    badge_name: str
    is_awarded: str  # TODO: cast to boolean ?
    date_awarded: str  # TODO: maybe cast to datetime ?
    hardcore_achieved: int  # TODO: boolean ?


class AwardedResponse(RAAPIResponse):
    num_possible_achievements: int
    possible_score: int
    num_achieved: int
    score_achieved: int
    num_achieved_hardcore: int
    score_achieved_hardcore: int


class RecentlyPlayedResponse(RAAPIResponse):
    game_id: int
    console_id: int
    console_name: str
    title: str
    image_icon: str
    image_title: str
    image_ingame: str
    image_box_art: str
    last_played: str  # TODO: maybe cast to datetime ?
    achievements_total: int


class UserSummaryResponse(RAAPIResponse):
    user: str
    member_since: str  # TODO: maybe cast it to date ?
    last_activity: LastActivityResponse
    rich_presence_msg: str
    last_game_id: int
    contrib_count: int
    contrib_yield: int
    total_points: int
    total_softcore_points: int
    total_true_points: int
    permissions: int
    untracked: int  # TODO: boolean ?
    id: int
    user_wall_active: int  # TODO: boolean ?
    motto: str
    rank: int
    recently_played_count: int
    recently_played: list[RecentlyPlayedResponse]
    awarded: dict[str, AwardedResponse]
    recent_achievements: dict[str, dict[str, RecentAchievementsResponse]]
    last_game: LastGameResponse | None = None
    user_pic: str
    total_ranked: int
    status: str  # TODO: maybe an enum ? "Offline" | ?


def get_user_summary(
    self: BaseRAClient, user: str, recent_games: int = 0, recent_cheevos: int = 10
) -> dict:
    """
    Get a user's exhaustive profile metadata

    Params:
        u: Username to query
        g: Number of recent games to fetch, default = 0
        a: Number of recent achievements to fetch, default = 10
    """
    response = self._call_api(
        "API_GetUserSummary.php",
        {"u": user, "g": recent_games, "a": recent_cheevos},
    )
    return UserSummaryResponse(**response)
