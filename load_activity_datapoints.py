import polars as pl
from utils import db_config
from psycopg2 import sql, connect
from typing import Iterable


def convert_to_str(q: sql.Composed, db_uri: str) -> str:
    try:
        with connect(db_uri) as conn:
            with conn.cursor() as cur:
                return q.as_string(cur)
    except Exception:
        raise
    finally:
        cur.close()
        conn.close()


def get_query(table: str, cols: Iterable[str],  db_uri: str) -> str:
    query = sql.SQL(
    """
    SELECT {cols} FROM {table}
    """
    ).format(
        cols=sql.SQL(', ').join(map(sql.Identifier, cols)),
        table=sql.Identifier(table)
    )
    
    return convert_to_str(query, db_uri)


src_db_uri = db_config.get_postgres_connection_string('postgres_staging')
dst_db_uri = db_config.get_postgres_connection_string('postgres_fb_05')
dst_table = 'activity_datapoints'

common_cols = ['src', 'timestamp']
tables_and_cols = {
    'account_activity': common_cols,
    'comments': common_cols,
    'comments_in_groups': common_cols,
    'ext_activity': common_cols,
    'pages_and_profiles_follow': common_cols,
    'pages_and_profiles_liked': common_cols,
    'photos': ['src', 'creation_timestamp'],
    'polls_voted_on': common_cols,
    'posts': common_cols,
    'posts_in_groups': common_cols,
    'profile_update_history': common_cols,
    'reactions': common_cols,
    'recently_viewed': common_cols,
    'recently_visited': common_cols,
    'saved_items': common_cols
}

dataframes = []
for table, cols in tables_and_cols.items():
    query = get_query(table, cols, src_db_uri)
    df = pl.read_database_uri(
        query,
        uri=src_db_uri,
        engine='connectorx'
    )
    if table == 'photos':
        df = df.rename({cols[1]: 'timestamp'})
    dataframes.append(df.unique(subset='timestamp'))

df = pl.concat(dataframes)
df = df.select(
    'src',
    (pl.col('timestamp') * 1000) \
    .cast(pl.Datetime ).dt.with_time_unit('ms').alias('timestamp')
)
df.write_database(
    table_name=dst_table,
    connection=dst_db_uri,
    if_exists='replace',
    engine='sqlalchemy'
)
