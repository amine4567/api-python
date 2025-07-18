from retroachievements import __version__
from retroachievements.base import BaseRAClient
from retroachievements.endpoints.game import get_game
from retroachievements.endpoints.user_points import get_user_points
from retroachievements.endpoints.user_summary import get_user_summary
from retroachievements.endpoints.game_extended import get_game_extended
from retroachievements.endpoints.achievement_count import get_achievement_count
from retroachievements.endpoints.achievement_distribution import (
    get_achievement_distribution,
)
from retroachievements.endpoints.console_ids import get_console_ids
from retroachievements.endpoints.game_list import get_game_list
from retroachievements.endpoints.user.unlocks import get_user_recent_achievements
from retroachievements.endpoints.user.unlocks import get_achievements_earned_between


class RAClient(BaseRAClient):
    # User endpoints
    get_user_points = get_user_points
    get_user_summary = get_user_summary
    get_recent_unlocks = get_user_recent_achievements
    get_achievements_earned_between = get_achievements_earned_between

    # Game endpoints
    get_game = get_game
    get_game_extended = get_game_extended

    get_achievement_count = get_achievement_count
    get_achievement_distribution = get_achievement_distribution

    # System Endpoints
    get_console_ids = get_console_ids
    get_game_list = get_game_list
