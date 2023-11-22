import polars as pl
from dataclasses import dataclass
from pathlib import Path


@dataclass
class PagesAndProfilesYouFollow:
    src_schema = {
        'pages_followed_v2': pl.List(
            pl.Struct(
                [
                    pl.Field('type_INTERNAL', pl.Utf8),
                    pl.Field('timestamp', pl.Int64),
                    pl.Field(
                        'data', pl.List(
                            pl.Struct(
                                [
                                    pl.Field('name', pl.Utf8)
                                ]
                            )
                        )
                    ),
                    pl.Field('title', pl.Utf8)
                ]
            )
        )
    }
    src_data = Path('pages_and_profiles/pages_and_profiles_you_follow.json')


@dataclass
class PagesAndProfilesYouLiked:
    src_schema = {
        'page_likes_v2': pl.List(
            pl.Struct(
                [
                    pl.Field('name', pl.Utf8),
                    pl.Field('timestamp', pl.Int64)
                ]
            )
        )
    }
    src_data = Path('pages_and_profiles/pages_you\'ve_liked.json')