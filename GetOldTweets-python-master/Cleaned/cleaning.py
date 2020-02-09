import preprocessor as p
from textblob import TextBlob
import csv
import os

tweets = list()
directory = "C:\\Users\\jingl\\OneDrive\\Documents\\GitHub\\DAP-Best-eggs\\GetOldTweets-python-master\\Exporter csv\\Hillary"
for filename in os.listdir(directory):
    if filename.endswith(".csv"): 
        print(filename)
        
        with open(directory + "\\" + filename, encoding='utf8', errors="ignore") as csvfile:
            next(csvfile)
            for row in csvfile:
                row = row.strip().split(";")
                tweets.append([row[1],p.clean(row[4].strip("\""))])

with open('hillary.csv', 'a', newline='', errors="ignore") as csvfile:
    writer = csv.writer(csvfile)
    for tweet in tweets:
        writer.writerow(tweet)





