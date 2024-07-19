from retroachievements.base import BaseRAClient


def get_console_ids(self: BaseRAClient) -> list:
    """
    Get the complete list of console ID and name pairs on the site

    Params:
        None
    """
    result = self._call_api("API_GetConsoleIDs.php?", {}).json()
    return result
