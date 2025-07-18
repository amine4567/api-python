import datetime


def convert_date_to_timestamp(date: datetime.date):
    dt_utc = datetime.datetime.combine(
        date, datetime.datetime.min.time(), tzinfo=datetime.timezone.utc
    )
    timestamp_utc = int(dt_utc.timestamp())
    return timestamp_utc
