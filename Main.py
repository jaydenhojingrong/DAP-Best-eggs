import sys
if sys.version_info[0] < 3:
    import got
else:
	import got3 as got

import pandas as pd
# def printTweet(descr, t):
# 	print(descr)
# 	print("Username: %s" % t.username)
# 	print("Retweets: %d" % t.retweets)
# 	print("Text: %s" % t.text)
# 	print("Mentions: %s" % t.mentions)
# 	print("Hashtags: %s\n" % t.hashtags)

	# # Example 1 - Get tweets by username
	# tweetCriteria = got.manager.TweetCriteria().setUsername('barackobama').setMaxTweets(1)
	# tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]

	# printTweet("### Example 1 - Get tweets by username [barackobama]", tweet)
tweetindiv = {}
runcheck = 0
datetens = 0
dateones = 0
prevdatetens = 0
prevdateones = 0
csv_counter = 0

# Example 2 - Get tweets by query search
for p in range(10):
	runcheck += 1

	if prevdateones == 9:
		prevdatetens += 1
		dateones = 0
	
	else:
		dateones += 1
	
	tweetCriteria = got.manager.TweetCriteria().setQuerySearch('trump').setSince(f'2016-06-{datetens}{dateones}').setNear("America").setUntil(f'2016-06-{datetens}{dateones+1}').setMaxTweets(5)
	prevdatetens = datetens
	prevdateones = dateones

# tweetCriteria = got.manager.TweetCriteria().setQuerySearch('trump').setSince("2016-05-20").setNear("America").setUntil("2016-05-21").setMaxTweets(50)
	count = 0
	for i in range(5):
		count += 1
		tweet = got.manager.TweetManager.getTweets(tweetCriteria)[i]
		tweetindiv["Trump " + str(count)] = [' ' + str(tweet.text), tweet.date]
		print(i)
		print([' ' + str(tweet.text), tweet.date]) 

		# tweetindiv["Date: "] = tweet.date
		# printTweet("### Example 2 - Get tweets by query search [Trump]", tweet)
	# count = 0
	# count += 1
	# tweetindiv = {}
	# tweetindiv[count] = tweet

	csv_counter += 1
	df = pd.DataFrame.from_dict(tweetindiv, orient = 'index')
	df.to_csv(f'Trump_looped_{csv_counter}.csv', index = True)

	with open(f'Trump_looped_{csv_counter}.csv', 'r') as file:
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
