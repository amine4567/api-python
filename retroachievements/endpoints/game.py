from retroachievements.base import BaseRAClient


def get_game(self: BaseRAClient, game: int) -> dict:
    """
    Get basic metadata about a game

    Params:
        i: The game ID to query
    """
    result = self._call_api("API_GetGame.php?", {"i": game}).json()
    return result
