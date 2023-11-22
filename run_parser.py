from json_parser import ParseJson
from utils import path_utils
from utils import db_config
from resources.schema.comments_and_reactions import Comments, PostsAndComments
from resources.schema.apps_and_websites_off_of_facebook import YourOffFacebookActivity
from resources.schema.groups import YourCommentsInGroups, YourPostsInGroups
from resources.schema.pages_and_profiles import PagesAndProfilesYouFollow, PagesAndProfilesYouLiked
from resources.schema.polls import PollsYouVotedOn
# from resources.schema.posts import YourPosts, YourUncategorizedPhotos
# from resources.schema.profile_information import ProfileUpdateHistory
# from resources.schema.saved_items_and_collections import YourSavedItems
# from resources.schema.security_and_login_information import AccountActivity
# from resources.schema.stories import StoryReactions
# from resources.schema.your_interactions_on_facebook import RecentlyViewed, RecentlyVisited
from resources.paths.paths import (
    BasePaths
)

raw_data_root = BasePaths.raw_data_base_path
stg_conn_str = db_config.get_postgres_connection_string('postgres_staging')

def parse_comments():
    table = 'comments'
    schema = Comments.src_schema
    src = path_utils.get_file_path(
        raw_data_root,
        Comments.src_data
    )
    ParseJson(table=table, conn_str=stg_conn_str).run(
        src=src,
        schema=schema
    )


def parse_posts_and_comments():
    table = 'reactions'
    schema = PostsAndComments.src_schema
    src = path_utils.get_file_path(
        raw_data_root,
        PostsAndComments.src_data
    )
    ParseJson(table=table, conn_str=stg_conn_str).run(
        src=src,
        schema=schema
    )

def parse_off_facebook_activity():
    table = 'ext_activity'
    schema = YourOffFacebookActivity.src_schema
    src = path_utils.get_file_path(
        raw_data_root,
        YourOffFacebookActivity.src_data
    )
    ParseJson(table=table, conn_str=stg_conn_str).run(
        src=src,
        schema=schema
    )

def parse_comments_in_groups():
    table = 'comments_in_groups'
    schema = YourCommentsInGroups.src_schema
    src = path_utils.get_file_path(
        raw_data_root,
        YourCommentsInGroups.src_data
    )
    ParseJson(table=table, conn_str=stg_conn_str).run(
        src=src,
        schema=schema
    )

def parse_posts_in_groups():
    table = 'posts_in_groups'
    schema = YourPostsInGroups.src_schema
    src = path_utils.get_file_path(
        raw_data_root,
        YourPostsInGroups.src_data
    )
    ParseJson(table=table, conn_str=stg_conn_str).run(
        src=src,
        schema=schema
    )


def parse_pages_and_profiles_follow():
    pass

def parse_pages_and_profiles_liked():
    pass

def parse_polls_voted_on():
    pass

def parse_posts():
    pass

def parse_uncategorized_photos():
    pass

def parse_profile_update_history():
    pass

def parse_saved_items():
    pass

def parse_account_activity():
    pass

def parse_story_reactions():
    pass

def parse_recently_viewed():
    pass

def parse_recently_visited():
    pass

def parse_all():
    parse_comments()
    parse_posts_and_comments()
    parse_off_facebook_activity()
    parse_comments_in_groups()
    parse_posts_in_groups()
    parse_pages_and_profiles_follow()
    parse_pages_and_profiles_liked()
    parse_polls_voted_on()
    parse_posts()
    parse_uncategorized_photos()
    parse_profile_update_history()
    parse_saved_items()
    parse_account_activity()
    parse_story_reactions()
    parse_recently_viewed()
    parse_recently_visited()
