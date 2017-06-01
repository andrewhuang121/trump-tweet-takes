#!/usr/bin/env python3 -tt
"""
File: console.py
---------------
Assignment 4: Trump Tweet Generator
Course: CS 41
Name: Andrew Huang
SUNet: ahuang98

Handles user interaction.

"""
import tweets
import language


def get_yes_or_no(prompt, reprompt=None):
    """
    Asks the user whether they would like to continue.
    Responses that begin with a `Y` return True. (case-insensitively)
    Responses that begin with a `N` return False. (case-insensitively)
    All other responses (including '') cause a reprompt.

    BORROWED FROM ASSIGN1: CRYPTO
    """
    if not reprompt:
        reprompt = prompt

    choice = input("{} (Y/N) ".format(prompt)).upper()
    while not choice or choice[0] not in ['Y', 'N']:
        choice = input(
            "Please enter either 'Y' or 'N'. {} (Y/N)? ".format(reprompt)).upper()
    return choice[0] == 'Y'


def main():
    """
    Handles the User I/O
    """
    print("Loading the Presidential Decrees...")
    donaldisms = tweets.get_tweets()

    print("Welcome to \"Ask Donald!\"")
    print()
    while True:
        print("Give us a word, and we'll see how the Donald feels about it.")
        word = "0"
        while not word.isalpha():
            word = input("Enter a word: ")

        print(
            language.generate_tweet(
                language.create_trigram_map(donaldisms),
                word))
        print()  # whitespace : - )
        print()

        if not get_yes_or_no("Generate again?"):
            print()
            print("Sad!")
            break


if __name__ == '__main__':
    main()
