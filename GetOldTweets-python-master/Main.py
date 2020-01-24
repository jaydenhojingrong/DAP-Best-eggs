import sys
if sys.version_info[0] < 3:
    import got
else:
	import got3 as got

import csv

def main():

	def printTweet(t):
		return([t.text, t.date])
		# print(descr)
		# print("Username: %s" % t.username)
		# print("Retweets: %d" % t.retweets)
		# print("Text: %s" % t.text)
		# print("Mentions: %s" % t.mentions)
		# print("Hashtags: %s\n" % t.hashtags)

	# Example 2 - Get tweets by query search
	tweetCriteria = got.manager.TweetCriteria().setQuerySearch('trump').setSince("2016-06-16").setNear("America").setUntil("2016-09-30").setMaxTweets(100)
	#print(len(got.manager.TweetManager.getTweets(tweetCriteria)))

	with open('data.csv', mode='w') as employee_file:
		employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		for i in range(10):
			tweet = got.manager.TweetManager.getTweets(tweetCriteria)[i]
			employee_writer.writerow(printTweet(tweet))	

if __name__ == '__main__':
	main()







# import sys
# if sys.version_info[0] < 3:
#     import got
# else:
# 	import got3 as got

# def main():

# 	def printTweet(descr, t):
# 		print(f'{descr}: {t.text} {t.date}')
		# print(descr)
		# print("Username: %s" % t.username)
		# print("Retweets: %d" % t.retweets)
		# print("Text: %s" % t.text)
		# print("Mentions: %s" % t.mentions)
		# print("Hashtags: %s\n" % t.hashtags)

	# # Example 1 - Get tweets by username
	# tweetCriteria = got.manager.TweetCriteria().setUsername('barackobama').setMaxTweets(1)
	# tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]

	# printTweet("### Example 1 - Get tweets by username [barackobama]", tweet)

	# Example 2 - Get tweets by query search
	# tweetCriteria = got.manager.TweetCriteria().setQuerySearch('trump').setSince("2016-06-16").setNear("America").setUntil("2016-09-30").setMaxTweets(100)
	#print(len(got.manager.TweetManager.getTweets(tweetCriteria)))
	# for i in range(10):
	# 	tweet = got.manager.TweetManager.getTweets(tweetCriteria)[i]

	# 	printTweet("### Example 2 - Get tweets including trump", tweet)

	# # Example 3 - Get tweets by username and bound dates
	# tweetCriteria = got.manager.TweetCriteria().setUsername("barackobama").setSince("2015-09-10").setUntil("2015-09-12").setMaxTweets(1)
	# tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]

	# printTweet("### Example 3 - Get tweets by username and bound dates [barackobama, '2015-09-10', '2015-09-12']", tweet)

# if __name__ == '__main__':
# 	main()
