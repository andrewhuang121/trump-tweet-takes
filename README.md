# Trumpisms

> Andrew Huang (ahuang98@stanford.edu)


## Overview

The Donald has tweeted about a lot of things, diseminating Trumpisms across the World Wide Web. But what if you wanted to know not his thoughts on avocado, rather than public policy or Rosie O' Donnell? This program will take the past tweets of the Clementine in Chief and spit back out a tweet about any word of your choosing!




## Background

This project is inspired large-in-part from CS106B's Serafini assignment, from when I took it under Chris (Piech & Gregg). This project is a great exercise in generating speech patterns at a decent level. It may be a stretch, but this project could easily be adapted to mimic someone else's Twitter, and could be the basis of things like chat-bots and programs of that ilk. I don't have a whole lot of experience with things like this outside of 106B, but I'm very excited to implement this. I came up with the idea while eating Taco Bell with my roommate and wondering what Trump thinks of the cool ranch Cheesy Gordita Crunch.



## Implementation Strategy


At a high-level, how do you plan to implement your project? How does it incorporate Python?

At a high level, there are four tasks: First, we have to grab el Presidente's tweets. Then, we have to build a 3-gram map from those tweets. Third, we will create a "tweet" from that map. Lastly, we swap out a word of identical part of speech for the word the user inputted.

A few packages will be essential. First and foremost, the Twitter API will be necessary in order to grab Cristiano Donaldo's axioms. Next, NLTK's excellent NLP modules will be essential in both gathering tri-grams and tagging parts of speech. I will compartmentalize the program into three parts: a console for user I/O, a file that contains all the Twitter processing, and a file containing all methods necessary for the NLP portions of the program.

User interaction will be done text-based within the terminal shell.

Twitter only allows for the grabbing of 200 tweets per requests, and 900 requests per 15 minutes. Luckily, even the Donald doesn't have that many tweets. We will grab all the tweets we can before starting the I/O process, to allow for the most current Trumpisms to be added to our corpus. Since Twitter's tweet ID's are time-sorted, we can grab all the tweets without overlap and we will know when we are done.

Tweet generation presents some interesting dilemnas. The 140 character limit shouldn't really be a problem, since we're modeling our tweets after strings with that limit already enforced. The difficult thing is creating coherent sentences from the map; in the 106B assignment, we started anywhere, and the user told the program how many words were to be generated. Here, we should ideally start at an actual starting word for a cogent thought, and end with a proper sentence. To get around this, we will use two heuristics: We want each tweet to start with a word that Trump tweeted beginning with a capital letter, and end it with a string token ending in some kind of ending punctuation. This isn't perfect, and there are ways to improve it, but in the interest of time, speed and complexity, this seems both necessary and sufficient.

NLTK provides two primary useful tools for this: a part-of-speech tagger and a tri-gram generator. The tri-gram generator immediately generates all tri-grams for a body of text, making the map generation infinitely easier. The part-of-speech tagger is necessary for inserting our desired word in a way that is likely to make sense. 

##Execution

In order to run this program, just run [`console.py`].

## Tasks
*This section is the most important because it gives us a sense of the scope of your project and forces you to think about the deliverables to which you'll hold yourself.*

1. Authenticate the Twitter API
2. Get all the tweets
3. Design the I/O
4. Build a tri-gram map
5. Generate a tweet from the map
6. Swap in the word that we want
7. (Stretch) Improve our heuristic so that we can create better tweets.
> Better capitalization analysis (uppercase, then lower case), keeping track of which words were tweeted first. We can also use NLTK's context tools to better extent.
8. (Stretch) Creating a sleeker interface for tweet generation, with graphics that actually look like a Trump tweet
9. (Stretch) Making an actual Twitter account from within Twitter's Python module and tweeting out our Gems.


## Resources
*This section is smaller and less vital than the others. If you're not using any external resources, you can leave this blank.*

The timeline of Donaldinho.

##Credits and Acknowledgements

Much thanks to Sam Redmond and the TA's for CS41 for such a great quarter. Also thanks to Chris Piech and Chris Gregg for the implementation inspiration from 106B. 