import polars as pl
from dataclasses import dataclass
from pathlib import Path


@dataclass
class YourPosts:
    src_schema = dict(
        pl.Struct(
            [
                pl.Field('type_INTERNAL', pl.Utf8),
                pl.Field('timestamp', pl.Int64),
                pl.Field(
                    'data', pl.List(
                        pl.Struct(
                            [
                                pl.Field('post', pl.Utf8)
                            ]
                        )
                    )
                ),
                pl.Field('title', pl.Utf8)
            ]
        )
    )
    src_data = Path('posts/your_posts_1.json')


@dataclass
class YourUncategorizedPhotos:
    src_schema = {
        'other_photos_v2': pl.List(
            pl.Struct(
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
                    )
                ]
            )
        )
    }
    src_data = Path('posts/your_uncategorized_photos.json')