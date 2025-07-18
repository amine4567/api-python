import time
from functools import reduce

from retroachievements import RAClient

user_name = "xxxx"
web_api_key = "xxxxxx"

client = RAClient(user_name, web_api_key)

# print("=======get_user_points=============")
# response = client.get_user_points("amine456")
# print(response)
# print("")
# time.sleep(1)

# print("=======get_user_summary no recent games=============")
# response = client.get_user_summary("amine456")
# print(response)
# print("")
# time.sleep(1)

# print("=======get_user_summary with recent games=============")
# response = client.get_user_summary("amine456", 5)
# print(response)
# print("")
# time.sleep(1)

# print("=======get_game=============")
# response = client.get_game(14402)
# print(response)
# print("")
# time.sleep(1)

# print("=======get_game_extended=============")
# response = client.get_game_extended(14402)
# print(response)
# print("")
# time.sleep(1)

# print("=======get_achievement_count=============")
# response = client.get_achievement_count(14402)
# print(response)
# print("")
# time.sleep(1)

# print("=======get_achievement_distribution=============")
# response = client.get_achievement_distribution(14402)
# print(response)
# print("")
# time.sleep(1)

# print("=======get_console_ids=============")
# response = client.get_console_ids()
# print(response)
# print("")
# time.sleep(1)

# print("=======get_game_list=============")
# response = client.get_game_list(24)
# print(response)
# print("")
# time.sleep(1)

print("=======get_recent_unlocks=============")
response = client.get_recent_unlocks("amine456", 5_300_000)  # 35 days
print(response)
print("")
time.sleep(1)

import polars as pl

df = pl.DataFrame(
    [(item.date, item.title, item.achievement_id) for item in response],
    schema=["date", "title", "achievement_id"],
)

characters = ["M", "A", "R", "I", "O"]
filter_condition = reduce(
    lambda acc, char: acc | pl.col("title").str.starts_with(char),
    characters,
    pl.col("title").str.starts_with(characters[0]),
)
filtered_df = (
    df.filter(filter_condition)
    # .rename({"date": "date_str"})
    .with_columns(
        [pl.col("date").str.strptime(pl.Datetime, "%Y-%m-%d %H:%M:%S").alias("date")]
    )
    .sort("date")
)
filtered_df.write_csv("sorted_data.csv")
