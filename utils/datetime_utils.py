import datetime
from typing import Union
from polars import col

def convert_epoch_time(epoch_time: Union[int, col]) -> datetime:
    return datetime.datetime.fromtimestamp(
        epoch_time
    ).strftime('%Y-%m-%d %H:%M:%S')
