import polars as pl
from dataclasses import dataclass
from pathlib import Path


@dataclass
class AccountActivity:
    src_schema = {
        'account_activity_v2': pl.List(
            pl.Struct(
                [
                    pl.Field('action', pl.Utf8),
                    pl.Field('timestamp', pl.Int64),
                    pl.Field('ip_address', pl.Utf8),
                    pl.Field('user_agent', pl.Utf8),
                    pl.Field('datr_cookie', pl.Utf8),
                    pl.Field('city', pl.Utf8),
                    pl.Field('region', pl.Utf8),
                    pl.Field('country', pl.Utf8),
                    pl.Field('site_name', pl.Utf8)
                ]
            )
        )
    }
    src_data = Path('security_and_login_information/account_activity.json')