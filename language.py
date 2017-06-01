#!/usr/bin/env python3 -tt
"""
File: language.py
---------------
Assignment 4: Trump Tweet Generator
Course: CS 41
Name: Andrew Huang
SUNet: ahuang98

Handles the NLP behind the program.

"""

import nltk
import collections
import random
import itertools

ending_punctuation = {'.', '?', '!'}  # finding the end of a sentence


def create_trigram_map(tweets):
    """
    Builds the tri-gram map. Tried several things, trigrams seems to work real well!

    @param tweets The tweetbase we're working off of.
    @return ngram_map The trigram map we're working with.
    """
    ngram_map = {}
    for tweet in tweets:
        # generate trigrams, into 3-tuples
        trigrams = list(nltk.trigrams(tweet.split(' ')))
        for (a, b, c) in trigrams:
            if (a, b) in ngram_map.keys():
                # tried default dict, but it ended up being messy as hell
                ngram_map[(a, b)].append(c)
            else:
                ngram_map[(a, b)] = [c]

    return ngram_map


def polish(new_tweet, word):
    """
    Polish the tweet! Add in the word.

    @param new_tweet The trigram generated tweet.
    @param word The word to be swapped into the tweet.
    @return final_tweet The final tweet
    """
    tagged_tweet = nltk.pos_tag(
        new_tweet)  # tag the parts of speech of the generated tweet

    # get the part of speech, look for the same part of speech
    tagged_word = nltk.pos_tag([word])
    tagged_word = tagged_word[0]  # strip the list from it; now just a tuple

    replaced = False
    final_tweet = []
    for token in tagged_tweet:  # replace the word
        if tagged_word[1] == token[1] and not replaced:  # same part of speech
            final_tweet.append(tagged_word[0])
            replaced = True
        else:
            final_tweet.append(token[0])

    return final_tweet


def generate_tweet(ngram_map, word):
    """
    Build the tweet using a ngram_map and a given word. Since unlike the 106B assignment,
    we have an indefinite number of words to generate, we implement two heuristics:

    Every tweet must start with a word with a capital letter.
    Every tweet must end with a ".", "?", or "!".

    @param ngram_map The trigram map used to build the tweet.
    @param word The word to be put in
    @return final_tweet The final completed tweet
    """
    first_words = random.choice(list(ngram_map.keys()))

    # if any of them are empty, they will be False
    if not first_words[0] and not first_words[1]:
        return generate_tweet(ngram_map, word)
    # we want the first letter to be capitalized: increases chance of being a
    # proper start to a sentence (decent heuristic), and the last token to
    # have some kind of ending punctuation.
    while not first_words[0][0].isupper(
    ) or first_words[1][-1] in ending_punctuation:
        first_words = random.choice(list(ngram_map.keys()))
        # if any of them are empty, they will be False
        if not first_words[0] and not first_words[1]:
            return generate_tweet(ngram_map, word)

    # from the first words, build the rest of the tweet.
    new_tweet = list(first_words)
    while new_tweet[-1][-1] not in ending_punctuation:
        if (new_tweet[-2], new_tweet[-1]) not in ngram_map.keys():
            # we've hit a bad point. try again!
            return generate_tweet(ngram_map, word)
        new_word = random.choice(ngram_map[(new_tweet[-2], new_tweet[-1])])
        if len(new_tweet) >= 1:
            new_tweet.append(new_word)

    final_tweet = polish(new_tweet, word)  # polish it

    if word not in final_tweet:
        # if it doesn't work, try again!
        return generate_tweet(ngram_map, word)

    return " ".join(final_tweet)  # final_tweet is a list
