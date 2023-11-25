import polars as pl
from dataclasses import dataclass
from pathlib import Path


@dataclass
class ProfileUpdateHistory:
    src_schema = {
        'profile_updates_v2': pl.List(
            pl.Struct(
                [
                    pl.Field('type_INTERNAL', pl.Utf8),
                    pl.Field('timestamp', pl.Int64),
                    pl.Field(
                        'data', pl.List(
                            pl.Struct(
                                [
                                    pl.Field('text', pl.Utf8)
                                ]
                            )
                        )
                    ),
                    pl.Field(
                        'attachments', pl.List(
                            pl.Struct(
                                [
                                    pl.Field(
                                        'data', pl.List(
                                            pl.Struct(
                                                [
                                                    pl.Field(
                                                        'media', pl.Struct(
                                                            [
                                                                pl.Field('uri', pl.Utf8),
                                                                pl.Field('media_path_INTERNAL', pl.Utf8),
                                                                pl.Field('type_INTERNAL', pl.Utf8),
                                                                pl.Field('creation_timestamp', pl.Int64),
                                                                pl.Field(
                                                                    'media_metadata', pl.Struct(
                                                                        [
                                                                            pl.Field(
                                                                                'photo_metadata', pl.Struct(
                                                                                    [
                                                                                        pl.Field(
                                                                                            'exif_data', pl.List(
                                                                                                pl.Struct(
                                                                                                    [
                                                                                                        pl.Field('upload_ip', pl.Utf8),
                                                                                                        pl.Field('taken_timestamp', pl.Int64)
                                                                                                    ]
                                                                                                )
                                                                                            )
                                                                                        )
                                                                                    ]
                                                                                )
                                                                            )
                                                                        ]
                                                                    )
                                                                ),
                                                                pl.Field('title', pl.Utf8),
                                                                pl.Field('description', pl.Utf8)
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
                    pl.Field('title', pl.Utf8)
                ]
            )
        )
    }
    src_data = Path('profile_information/profile_update_history.json')