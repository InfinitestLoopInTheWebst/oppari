import polars as pl
from dataclasses import dataclass
from pathlib import Path


@dataclass
class RecentlyViewed:
    src_schema = {
        'recently_viewed': pl.List(
            pl.Struct(
                [
                    pl.Field('name', pl.Utf8),
                    pl.Field('description', pl.Utf8),
                    pl.Field(
                        'children', pl.List(
                            pl.Struct(
                                [
                                    pl.Field('name', pl.Utf8),
                                    pl.Field('description', pl.Utf8),
                                    pl.Field(
                                        'entries', pl.List(
                                            pl.Struct(
                                                [
                                                    pl.Field('timestamp', pl.Int64),
                                                    pl.Field(
                                                        'data', pl.Struct(
                                                            [
                                                                pl.Field('name', pl.Utf8),
                                                                pl.Field('uri', pl.Utf8),
                                                                pl.Field('watch_time', pl.Utf8),
                                                                pl.Field('watch_position_seconds', pl.Utf8),
                                                                pl.Field('value', pl.Utf8)
                                                            ]
                                                        )
                                                    ),
                                                ]
                                            )
                                        )
                                    )
                                ]
                            )
                        )
                    ),
                    pl.Field(
                        'entries', pl.List(
                            pl.Struct(
                                [
                                    pl.Field('timestamp', pl.Int64),
                                    pl.Field(
                                        'data', pl.Struct(
                                            [
                                                pl.Field('name', pl.Utf8),
                                                pl.Field('uri', pl.Utf8),
                                                pl.Field('value', pl.Utf8)
                                            ]
                                        )
                                    ),
                                ]
                            )
                        )
                    )
                ]
            )
        )
    }
    src_data = Path('your_interactions_on_facebook/recently_viewed.json')


@dataclass
class RecentlyVisited:
    src_schema = {
        'visited_things_v2': pl.List(
            pl.Struct(
                [
                    pl.Field('name', pl.Utf8),
                    pl.Field('description', pl.Utf8),
                    pl.Field(
                        'entries', pl.List(
                            pl.Struct(
                                [
                                    pl.Field('timestamp', pl.Int64),
                                    pl.Field(
                                        'data', pl.Struct(
                                            [
                                                pl.Field('name', pl.Utf8),
                                                pl.Field('uri', pl.Utf8),
                                                pl.Field('value', pl.Utf8)
                                            ]
                                        )
                                    ),
                                ]
                            )
                        )
                    ),
                ]
            )
        )
    }
    src_data = Path('your_interactions_on_facebook/recently_visited.json')