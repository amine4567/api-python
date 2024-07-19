from retroachievements.base import BaseRAClient


def get_user_points(self: BaseRAClient, user: str) -> dict:
    """
    Get a user's total hardcore and softcore points

    Params:
        u: Username to query
    """
    result = self._call_api("API_GetUserPoints.php?", {"u": user}).json()
    return result
