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


@dataclass
class CommentsAndReactions:
    parent_folder = Path('comments_and_reactions')
    json_comments = Path('comments.json')
    json_posts_and_comments = Path('posts_and_comments.json')


@dataclass
class AppsAndWebsitesOffOfFacebook:
    parent_folder = Path('apps_and_websites_off_of_facebook')
    json_your_off_facebook_activity = Path('your_off-facebook_activity.json')