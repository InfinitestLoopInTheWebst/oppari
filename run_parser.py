from json_parser import ParseJson
from utils import path_utils
from utils import db_config
from resources.schema.comments_and_reactions import Comments, PostsAndComments
from resources.schema.apps_and_websites_off_of_facebook import YourOffFacebookActivity
from resources.schema.groups import YourCommentsInGroups, YourPostsInGroups
from resources.schema.pages_and_profiles import PagesAndProfilesYouFollow, PagesAndProfilesYouLiked
from resources.schema.polls import PollsYouVotedOn
from resources.schema.posts import YourPosts, YourUncategorizedPhotos
from resources.schema.profile_information import ProfileUpdateHistory
from resources.schema.saved_items_and_collections import YourSavedItems
from resources.schema.security_and_login_information import AccountActivity
from resources.schema.your_interactions_on_facebook import RecentlyViewed, RecentlyVisited
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
    table = 'pages_and_profiles_follow'
    schema = PagesAndProfilesYouFollow.src_schema
    src = path_utils.get_file_path(
        raw_data_root,
        PagesAndProfilesYouFollow.src_data
    )
    ParseJson(table=table, conn_str=stg_conn_str).run(
        src=src,
        schema=schema
    )

def parse_pages_and_profiles_liked():
    table = 'pages_and_profiles_liked'
    schema = PagesAndProfilesYouLiked.src_schema
    src = path_utils.get_file_path(
        raw_data_root,
        PagesAndProfilesYouLiked.src_data
    )
    ParseJson(table=table, conn_str=stg_conn_str).run(
        src=src,
        schema=schema
    )

def parse_polls_voted_on():
    table = 'polls_voted_on'
    schema = PollsYouVotedOn.src_schema
    src = path_utils.get_file_path(
        raw_data_root,
        PollsYouVotedOn.src_data
    )
    ParseJson(table=table, conn_str=stg_conn_str).run(
        src=src,
        schema=schema
    )

def parse_posts():
    table = 'posts'
    schema = YourPosts.src_schema
    src = path_utils.get_file_path(
        raw_data_root,
        YourPosts.src_data
    )
    ParseJson(table=table, conn_str=stg_conn_str).run(
        src=src,
        schema=schema
    )

def parse_uncategorized_photos():
    table = 'photos'
    schema = YourUncategorizedPhotos.src_schema
    src = path_utils.get_file_path(
        raw_data_root,
        YourUncategorizedPhotos.src_data
    )
    ParseJson(table=table, conn_str=stg_conn_str).run(
        src=src,
        schema=schema
    )

def parse_profile_update_history():
    table = 'profile_update_history'
    schema = ProfileUpdateHistory.src_schema
    src = path_utils.get_file_path(
        raw_data_root,
        ProfileUpdateHistory.src_data
    )
    ParseJson(table=table, conn_str=stg_conn_str).run(
        src=src,
        schema=schema
    )

def parse_saved_items():
    table = 'saved_items'
    schema = YourSavedItems.src_schema
    src = path_utils.get_file_path(
        raw_data_root,
        YourSavedItems.src_data
    )
    ParseJson(table=table, conn_str=stg_conn_str).run(
        src=src,
        schema=schema
    )

def parse_account_activity():
    table = 'account_activity'
    schema = AccountActivity.src_schema
    src = path_utils.get_file_path(
        raw_data_root,
        AccountActivity.src_data
    )
    ParseJson(table=table, conn_str=stg_conn_str).run(
        src=src,
        schema=schema
    )

def parse_recently_viewed():
    table = 'recently_viewed'
    schema = RecentlyViewed.src_schema
    src = path_utils.get_file_path(
        raw_data_root,
        RecentlyViewed.src_data
    )
    ParseJson(table=table, conn_str=stg_conn_str).run(
        src=src,
        schema=schema
    )

def parse_recently_visited():
    table = 'recently_visited'
    schema = RecentlyVisited.src_schema
    src = path_utils.get_file_path(
        raw_data_root,
        RecentlyVisited.src_data
    )
    ParseJson(table=table, conn_str=stg_conn_str).run(
        src=src,
        schema=schema
    )

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
    parse_recently_viewed()
    parse_recently_visited()
