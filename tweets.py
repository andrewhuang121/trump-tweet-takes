#!/usr/bin/env python3 -tt
"""
File: tweets.py
---------------
Assignment 4: Trump Tweet Generator
Course: CS 41
Name: Andrew Huang
SUNet: ahuang98

Grabs the Donald's Tweets, using Twitter's API.

"""

import twitter

_api #put api here


def get_tweets():
    """
    Grabs tweets from the Donald's timeline, excluding RT's and replies.

    @return tweets Giant list of all the tweets we can grab
    """
    numrequests = 900
    username = "realDonaldTrump"
    statuses = _api.GetUserTimeline(
        screen_name=username,
        include_rts=False,
        exclude_replies=True,
        count=200)  # can only grab 200 tweets at a time
    tweets = [s.text for s in statuses]
    old_id = statuses[-1].id  # get the ID of the oldest tweet in the batch
    old = tweets
    for i in range(numrequests):  # don't max out, even though highly unlikely
        statuses = _api.GetUserTimeline(
            screen_name=username,
            include_rts=False,
            exclude_replies=True,
            count=200,
            max_id=old_id)
        if statuses[-1].id == old_id:  # we've gotten ALL THE TWEETS
            break
        tweets += [s.text for s in statuses]  # add the tweets
        old_id = statuses[-1].id  # update the old id

    return tweets
