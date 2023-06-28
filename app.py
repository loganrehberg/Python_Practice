# the statement import is used to make the code in one module available in another, in this case I imported praw, which stands for Python Reddit API wrapper.
# import config which is a configuration scheme with support for mapping.
# import time which creates various time-related functions, in this case time.sleep
# import os which adds various misc. os functions
import praw
from praw.models.reddit import comment

import config
import time
import os


## def is a function parameter which in this case is defining for the user when the bot is logging in.
def bot_login():
    print()
    "Logging in"
    r = praw.Reddit(username=config.username,
                    password=config.password,
                    client_id=config.client_id,
                    client_secret=config.client_secret,
                    user_agent="Reddit commenter")
    print()
    "Logged in"
    return r


# this is a function parameter to run the bot, print searching, and to set the limit of the comments searched which the user posted to 1000
def run_bot(r, comments_replied_to):
    print()
    "searching last 1,000 comments"

    for comment in r.subreddit('test').comments(limit=1000):
        if "sample user comment" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
            print()
            "string with \"sample user comment\" found in comment " + comment.id
            comment.reply("..")
            print()
            "Replied " + comment.id

            comments_replied_to.append(comment.id)

            with open("comments_replied_to.text", "a") as f:
                f.write(comment.id + "\n")

        print()
        "search complete"

        print()
        comments_replied_to

        print()
        "Sleeping zzz mimimi"
        time.sleep(10)


# this a function parameter to check if the specified path is within the os files, if not it does, it mutes the comments replied to. If it is, it opens comments replied to as a formatted string and splits + creats a new line
def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comment.split("\n")
            comments_replied_to = filter(None, comments_replied_to)
    return comments_replied_to


r = bot_login()
comments_replied_to = get_saved_comments()
print()
comments_replied_to

while True:
    run_bot(r, comments_replied_to)
