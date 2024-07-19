from retroachievements.base import BaseRAClient


def get_game_list(
    self: BaseRAClient, system: int, has_cheevos: int = 0, hashes: int = 0
) -> dict:
    """
    Get the complete list of games for a console

    Params:
        i: The system ID to query
        f: If 1, only returns games that have achievements (default = 0)
        h: If 1, also return the supported hashes for games (default = 0)
    """
    result = self._call_api(
        "API_GetGameList.php?", {"i": system, "f": has_cheevos, "h": hashes}
    ).json()
    return result
