import preprocessor as p
from textblob import TextBlob
import csv
import os
import sys

'''
Output format is:
{username1: (date1, [sentence1, sentence2]), date2, [sentence1, sentence2], username2: ....}
    ^key     ^ tuple with date and tweet sentences          ^ tweet sentences is a list
'''

tweets = dict()
user = str()
pre_clean_tweet = str()
cleaned_tweet = list()

#keyword = input("Enter: \n [1] for trump \n [2] for hillary \n [3] for clinton \n")
keyword = "3"
if (keyword == "1"):
    keyword = "Trump"
elif (keyword == "2"):
    keyword = "Hillary"
elif (keyword == "3"):
    keyword = "Clinton"
else:
    print("errrr......")
    sys.exit()

directory = "C:\\Users\\jingl\\OneDrive\\Documents\\GitHub\\DAP-Best-eggs\\GetOldTweets-python-master\\Exporter csv\\" + keyword

#loop thru all csv in the above directory
for filename in os.listdir(directory):
    if filename.endswith(".csv"): 
        print(filename)
        
        with open(directory + "\\" + filename, encoding='utf8', errors="ignore") as csvfile:
            #skip column headers
            next(csvfile)
            for row in csvfile:
                #in clinton file, we ignore tweets with hillary keyword inside
                #to avoid duplicates
                if (keyword == "Clinton"):
                    if ("hillary" in row.lower()):
                        continue
                #data delimiter is seperated by ;
                row = row.strip().split(";")

                #split URL to extract username
                user = row[-1].split("/")
                user = user[3]

                #split actual tweet by sentence and clean each sentence
                pre_clean_tweet = TextBlob(row[4].strip("\""))
                pre_clean_tweet = pre_clean_tweet.sentences

                for sentence in pre_clean_tweet:
                    sentence = p.clean(str(sentence))
                    cleaned_tweet.append(sentence)
                
                #populate dictionary
                if (user in tweets):
                    tweets[user].append(tuple((row[1], cleaned_tweet)))
                else:
                    tweets[user] = [tuple((row[1], cleaned_tweet))]
                #reset clean_tweet
                cleaned_tweet = list()

#populate csv
with open(keyword + '.csv', 'a', newline='', errors="ignore") as csvfile:
    writer = csv.DictWriter(csvfile, ["user", "tweets"])
    for user, date_tweet in tweets.items():
        writer.writerow({"user": user + str(date_tweet)})







