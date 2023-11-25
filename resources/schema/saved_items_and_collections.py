import polars as pl
from dataclasses import dataclass
from pathlib import Path


@dataclass
class YourSavedItems:
    src_schema = {
        'saves_v2': pl.List(
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
                                                                pl.Field('name', pl.Utf8),
                                                                pl.Field('source', pl.Utf8), 
                                                                pl.Field('url', pl.Utf8)
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
    src_data = Path('saved_items_and_collections/your_saved_items.json')