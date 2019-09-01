import tweepy
import time
import networkx as nx


consumer_key = "OoeWy46Lc4zBVnf6I0zJSzZrJ"
consumer_secret  = "dS9jqv6nNTkxEU3XfyMTTFURyUGwxEbuvweHKpJ2TRMhTB9fHN"
access_token = "1145945437150384128-PJm1ZH584144AmlGqwxdgLfsQKvLZl"
access_token_secret = "Bdo2WDq2qIZ4tsBocJaJewz2SzEjBzSyX3t7DHLGx5xl1"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# f = open('predictUser.txt', 'r')
f = open('./testUserDONE.txt', 'r')
userStr = f.read()
userDict = eval(userStr)
userGraph = nx.DiGraph(userDict)

userList = list(userGraph.nodes)


tweet_count_dict = {}

count = 0
error_count = 0

for userName in userList:
    try:
        user = api.get_user(userName)
        user_count = user.statuses_count
        tweet_count_dict[userName] = user_count
        count += 1
        print("user: %s ; tweets: %d ; count : %d" %(userName, user_count, count))

        if count % 100 == 0:
            output = open('userTweetsCountTest.txt', 'w')
            tweet_count_dict_str = str(tweet_count_dict)
            output.write(tweet_count_dict_str)
            output.close()

    except tweepy.error.TweepError as te:
        error_count += 1
        print("error")
        print("error_count: %d" %(error_count))
        
        time_now = time.time()
        if error_count > 1 and (time.time() - time_prev < 3):
            time.sleep(900)
            time_prev = time.time()
        else:
            time_prev = time.time()
            continue

#export
output = open('userTweetsCountTestDONE.txt', 'w')
tweet_count_dict_str = str(tweet_count_dict)
output.write(tweet_count_dict_str)
output.close()






