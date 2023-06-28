import praw
import config
import time
import os

def bot_login():
    print "logging in"
    r = praw.Reddit(username = config.username,
                    password = config.password,
                    client_id = config.client_id,
                    client_secret = config.client_secret,
                    user_agent = "Reddit commenter")
    print "logged in"

