from retroachievements.base import BaseRAClient
from retroachievements.models import RAAPIResponse


class GameResponse(RAAPIResponse):
    title: str
    game_title: str
    console_id: int
    console_name: str
    console: str
    forum_topic_id: int
    flags: int
    game_icon: str
    image_icon: str
    image_title: str
    image_ingame: str
    image_box_art: str
    publisher: str
    developer: str
    genre: str
    released: str


def get_game(self: BaseRAClient, game: int) -> dict:
    """
    Get basic metadata about a game

    Params:
        i: The game ID to query
    """
    result = self._call_api("API_GetGame.php?", {"i": game})
    return GameResponse(**result)
