from retroachievements.base import BaseRAClient


def get_achievement_distribution(self: BaseRAClient, game: int) -> dict:
    """
    Get how many players have unlocked how many achievements for a game

    Params:
        i: The game ID to query
    """
    result = self._call_api("API_GetAchievementDistribution.php?", {"i": game}).json()
    return result
