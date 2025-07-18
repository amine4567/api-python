import datetime
import time

import polars as pl

from retroachievements import RAClient

MAX_SIZE = 500

user_name = "xxxxx"
web_api_key = "xxxxxx"

start_date = datetime.date(2014, 1, 1)
end_date = datetime.date(2024, 10, 31)


client = RAClient(user_name, web_api_key)

response_size = MAX_SIZE
from_date = start_date
results = []
while response_size >= MAX_SIZE:
    print(f"Calling from {from_date} to {end_date}")
    response = client.get_achievements_earned_between(
        "amine456", from_date=from_date, to_date=end_date
    )
    time.sleep(2)

    df = pl.DataFrame(response).with_columns(
        pl.col("date").str.strptime(pl.Datetime, "%Y-%m-%d %H:%M:%S").alias("datetime")
    )
    results.append(df)
    response_size = df.height
    from_date = df["datetime"].max().date()

unlocks = (
    pl.concat(results)
    .unique(subset="achievement_id")
    .with_columns((pl.col("true_ratio") / pl.col("points")).alias("retro_ratio"))
    .sort(by="retro_ratio", descending=True)
)
unlocks.write_csv("unlocks.csv")
