from pykeepass import PyKeePass
import sys
sys.path.append('C:/Koodailut/oppari/code/python')
from  resources.paths.paths import Secrets, BasePaths
from utils.path_utils import get_file_path


pw_file = get_file_path(
    BasePaths.resource_base_path,
    Secrets.parent_folder,
    Secrets.passfile
)
pw_db = get_file_path(
    BasePaths.resource_base_path,
    Secrets.parent_folder,
    Secrets.pw_database,
    return_type=str
)


def get_pw():
    with open(pw_file, 'rt') as f:
        pw = f.readline()
    return pw

def get_conn_config(db_name: str):
    kp = PyKeePass(pw_db, password=get_pw())
    entry = kp.find_entries(title=db_name, first=True)
    
    return entry.username, \
        entry.password, \
        entry.get_custom_property('dbname'), \
        entry.get_custom_property('server'), \
        entry.get_custom_property('port')
