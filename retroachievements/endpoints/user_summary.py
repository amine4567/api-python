from retroachievements.base import BaseRAClient


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
    result = self._call_api(
        "API_GetUserSummary.php?",
        {"u": user, "g": recent_games, "a": recent_cheevos},
    ).json()
    return result
