import datetime

from retroachievements import RAClient

user_name = "xxxxx"
web_api_key = "xxxxxxx"

gc_system_id = 16

start_date = datetime.date(2014, 1, 1)
end_date = datetime.date(2024, 10, 31)


client = RAClient(user_name, web_api_key)

games = client.get_game_list(gc_system_id, 1)

pass
