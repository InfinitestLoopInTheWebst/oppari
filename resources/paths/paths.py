from dataclasses import dataclass
from pathlib import Path


@dataclass
class BasePaths:
    resource_base_path = Path('C:/Koodailut/oppari/code/resources')
    raw_data_base_path = Path('C:/Koodailut/oppari/data/extracted')


@dataclass
class Secrets:
    parent_folder = Path('db_config')
    passfile = Path('passfile')
    pw_database = Path('passwords.kdbx')
