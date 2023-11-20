from utils.kp_utils import get_conn_config

def get_postgres_connection_string(db_name: str):
    user, pw, db, server, port = get_conn_config(db_name)
    return f'postgresql://{user}:{pw}@{server}:{port}/{db}'
