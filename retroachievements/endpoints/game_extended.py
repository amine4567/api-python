from retroachievements.base import BaseRAClient


def get_game_extended(self: BaseRAClient, game: int) -> dict:
    """
    Get extended metadata about a game

    Params:
        i: The game ID to query
    """
    result = self._call_api("API_GetGameExtended.php?", {"i": game}).json()
    return result
