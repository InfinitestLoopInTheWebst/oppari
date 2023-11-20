import polars as pl
from dataclasses import dataclass
from pathlib import Path

@dataclass
class YourCommentsInGroups:
    src_schema = {
        'group_comments_v2': pl.List(
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
                                                        'external_context', pl.Struct(
                                                            [
                                                                pl.Field('url', pl.Utf8)
                                                            ]
                                                        )
                                                    ),
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
                                                                )
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
                    pl.Field(
                        'data', pl.List(
                            pl.Struct(
                                [
                                    pl.Field(
                                        'comment', pl.Struct(
                                            [
                                                pl.Field('timestamp', pl.Int64),
                                                pl.Field('comment', pl.Utf8),
                                                pl.Field('author', pl.Utf8),
                                                pl.Field('group', pl.Utf8)
                                            ]
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
    src_data = Path('groups/your_comments_in_groups.json')


@dataclass
class YourPostsInGroups:
    src_schema = {
        'group_posts_v2': pl.List(
            pl.Struct(
                [
                    pl.Field('type_INTERNAL_header', pl.Utf8),
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
                                                        'external_context', pl.Struct(
                                                            [
                                                                pl.Field('url', pl.Utf8)
                                                            ]
                                                        )
                                                    ),
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
                                                                )
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
                    pl.Field('data', pl.List(
                        pl.Struct(
                            [
                                pl.Field('post', pl.Utf8)
                            ]
                        )
                    )),
                    pl.Field('title', pl.Utf8)
                ]
            )
        )
    }
    src_data = Path('groups/your_posts_in_groups.json')