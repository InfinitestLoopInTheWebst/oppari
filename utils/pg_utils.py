import psycopg2
from psycopg2 import sql
from psycopg2.sql import Composable
from psycopg2.extras import DictCursor
from typing import Optional, Any, Collection


def execute_query(
    conn_config: dict,
    sql: str,
    cursor_factory: Optional[Any]=None
):
    conn = _connect(conn_config)
    try:
        with conn.cursor(cursor_factory=cursor_factory) as cur:
            cur.execute(sql)
            cur.fetchall()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def _connect(
    conn_config: dict
):
    conn = psycopg2.connect(
        **conn_config
    )
    return conn
