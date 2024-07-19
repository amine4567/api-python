from retroachievements.base import BaseRAClient


def get_achievement_count(self: BaseRAClient, game: int) -> dict:
    """
    Get the list of achievement ID's for a game

    Params:
        i: The game ID to query
    """
    result = self._call_api("API_GetAchievementCount.php?", {"i": game}).json()
    return result
