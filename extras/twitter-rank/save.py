import csv

with open('./user_tweets_count_PREDICT.csv') as data:
    reader = csv.reader(data)
    user_list = list(row[0] for row in reader)
with open('./user_tweets_count_PREDICT.csv') as data:
    reader = csv.reader(data)
    count_list = list(row[1] for row in reader)

dict1 = {}
for i in range(0, len(count_list)):
    dict1[user_list[i]] = count_list[i]

print(dict1)

output = open('./data/userTweetsCount_PREDICT.txt','w')
output.write(str(dict1))
output.close()
