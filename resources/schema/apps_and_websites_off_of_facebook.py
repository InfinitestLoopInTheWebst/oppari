import polars as pl
from dataclasses import dataclass
from pathlib import Path

@dataclass
class YourOffFacebookActivity:
    src_schema = {
        'off_facebook_activity_v2': pl.List(
            pl.Struct(
                [
                    pl.Field('name', pl.Utf8),
                    pl.Field(
                        'events', pl.List(
                            pl.Struct(
                                [
                                    pl.Field('id', pl.Int64),
                                    pl.Field('type', pl.Utf8),
                                    pl.Field('timestamp', pl.Int64)
                                ]
                            )
                        )
                    )
                ]
            )
        )
    }
    src_data = Path('apps_and_websites_off_of_facebook/your_off-facebook_activity.json')