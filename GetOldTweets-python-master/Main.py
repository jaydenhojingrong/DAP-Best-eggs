import sys
if sys.version_info[0] < 3:
    import got
else:
	import got3 as got

def printTweet(descr, t):
	print(descr)
	print("Username: %s" % t.username)
	print("Retweets: %d" % t.retweets)
	print("Text: %s" % t.text)
	print("Mentions: %s" % t.mentions)
	print("Hashtags: %s\n" % t.hashtags)

	# # Example 1 - Get tweets by username
	# tweetCriteria = got.manager.TweetCriteria().setUsername('barackobama').setMaxTweets(1)
	# tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]

	# printTweet("### Example 1 - Get tweets by username [barackobama]", tweet)
tweetindiv = {}
# Example 2 - Get tweets by query search
tweetCriteria = got.manager.TweetCriteria().setQuerySearch('trump').setSince("2016-05-01").setNear("Singapore").setUntil("2016-09-30").setMaxTweets(10)
count = 0
for i in range(10):
	count += 1
	tweet = got.manager.TweetManager.getTweets(tweetCriteria)[i]
	tweetindiv["Trump " + str(count)] = [' ' + str(tweet.text), tweet.date]
	# tweetindiv["Date: "] = tweet.date
	# printTweet("### Example 2 - Get tweets by query search [Trump]", tweet)
print(tweetindiv)

import pandas as pd

# count = 0
# count += 1
# tweetindiv = {}

# tweetindiv[count] = tweet
df = pd.DataFrame.from_dict(tweetindiv, orient = 'index')
df.to_csv('test.csv', index = True)

with open('test.csv', 'r') as file:
	for line in file:
		print(line)
# df = pd.DataFrame.from_dict(productdictionary,orient='index')
# display(df)
	# # Example 3 - Get tweets by username and bound dates
	# tweetCriteria = got.manager.TweetCriteria().setUsername("barackobama").setSince("2015-09-10").setUntil("2015-09-12").setMaxTweets(1)
	# tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]

	# printTweet("### Example 3 - Get tweets by username and bound dates [barackobama, '2015-09-10', '2015-09-12']", tweet)

# if __name__ == '__main__':
# 	main()
