import polars as pl
from dataclasses import dataclass
from pathlib import Path


@dataclass
class PollsYouVotedOn:
    src_schema = {
        'poll_votes_v2': pl.List(
            pl.Struct(
                [
                    pl.Field('type_INTERNAL', pl.Utf8),
                    pl.Field('timestamp', pl.Int64),
                    pl.Field(
                        'attachments', pl.List(
                            pl.Struct(
                                [
                                    pl.Field(
                                        'data', pl.List(
                                            pl.Struct(
                                                [
                                                    pl.Field(
                                                        'options', pl.Struct(
                                                            [
                                                                pl.Field('option', pl.Utf8),
                                                                pl.Field('voted', pl.Boolean)
                                                            ]
                                                        )
                                                    )
                                                ]
                                            )
                                        )
                                    )
                                ]
                            )
                        )
                    ),
                    pl.Field('title', )
                ]
            )
        )
    }
    src_data = Path('polls/polls_you_voted_on.json')