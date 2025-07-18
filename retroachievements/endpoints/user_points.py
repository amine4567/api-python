from retroachievements.base import BaseRAClient
from retroachievements.models import RAAPIResponse


class UserPointsResponse(RAAPIResponse):
    points: int
    softcore_points: int


def get_user_points(self: BaseRAClient, user: str):
    """
    Get a user's total hardcore and softcore points

    Params:
        u: Username to query
    """
    response = self._call_api("API_GetUserPoints.php", {"u": user})
    return UserPointsResponse(**response)
