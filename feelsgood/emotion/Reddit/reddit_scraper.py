import praw
from random import randint
import webbrowser
from . import subreddits


def getRedditInstance():
	"""
	Get the Reddit instance to make API calls. 

	"""

	reddit = praw.Reddit('bot1')

	return reddit

def getSubredditInstance(reddit, subreddit):
	"""
	Get subreddit instance from specified subreddit string.

	"""

	sub = reddit.subreddit(subreddit)

	return sub

def getRandomSubmission(subreddit):
	"""
	Get random subreddit submission from specified subreddit instance.

	"""
	index = randint(0, 100)
	topMonthlyPosts = subreddit.top('month')

	randomSubmission = list(topMonthlyPosts)[index].url

	return randomSubmission

def pickSubreddit(emotion):
	"""
	Pick a subreddit based on specified emotion.
	"""
	return EMOTION_DICTIONARY[emotion]

def getContent(emotion):
	"""
	Get random content based on specified emotion.
	"""
	reddit = getRedditInstance()
	pickedSub = pickSubreddit(emotion);
	subreddit = getSubredditInstance(reddit, pickedSub)
	randomSubmission = getRandomSubmission(subreddit)

	return randomSubmission
	
if __name__ == "__main__":

	#testing reddit scraping
	reddit = getRedditInstance()
	pickedSub = pickSubreddit("sad");
	subreddit = getSubredditInstance(reddit, pickedSub)
	randomSubmission = getRandomSubmission(subreddit)
	webbrowser.open(randomSubmission)

	

