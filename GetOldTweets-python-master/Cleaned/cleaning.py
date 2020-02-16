import preprocessor as p
from textblob import TextBlob
import csv
import os
import sys

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

for filename in os.listdir(directory):
    if filename.endswith(".csv"): 
        print(filename)
        
        with open(directory + "\\" + filename, encoding='utf8', errors="ignore") as csvfile:
            next(csvfile)
            for row in csvfile:
                if (keyword == "Clinton"):
                    if ("hillary" in row.lower()):
                        continue

                row = row.strip().split(";")

                user = row[-1].split("/")
                user = user[3]

                pre_clean_tweet = TextBlob(row[4].strip("\""))
                pre_clean_tweet = pre_clean_tweet.sentences

                for sentence in pre_clean_tweet:
                    sentence = p.clean(str(sentence))
                    cleaned_tweet.append(sentence)

                if (user in tweets):
                    tweets[user].append(tuple((row[1], cleaned_tweet)))
                else:
                    tweets[user] = [tuple((row[1], cleaned_tweet))]

                cleaned_tweet = list()

with open(keyword + '.csv', 'a', newline='', errors="ignore") as csvfile:
    writer = csv.DictWriter(csvfile, ["user", "tweets"])
    for user, date_tweet in tweets.items():
        writer.writerow({"user": user + str(date_tweet)})







