import networkx as nx
import twint


f = open('./data/network_TEST_DONE.txt', 'r')
# f = open('./data/network_PREDICT_DONE.txt', 'r')
userDict = eval(f.read())
userGraph = nx.DiGraph(userDict)

userList = list(userGraph.nodes)
userList.sort()

# NEED TO CHANGE
userList = [userList[i] for i in range(0, 100)]

userTopicDict = {}
userRetweetDict = {}
topic_tweet_Dict = {}

for user in userList:
    
    print(user)
    c = twint.Config()
    c.Username = user
    c.Store_object = True
    c.Search = "movie OR cinema OR film OR theater"
    twint.run.Search(c)

    tweets_count = len(twint.output.tweets_list)
    topic_tweet_Dict[user] = tweets_count

    Topic_count = 0
    retweetCount = 0

    for tweet in twint.output.tweets_list:
        tweet_str = str(tweet.tweet)
        retweetCount += int(tweet.retweets_count)
        Topic_count += tweet_str.count('movie') + tweet_str.count('film') + tweet_str.count('theater') + tweet_str.count('cinema')

    userTopicDict[user] = Topic_count
    userRetweetDict[user] = retweetCount


    print()
    print()
    print()
    print()
    print(topic_tweet_Dict)
    print(userRetweetDict)
    print(userTopicDict)

    # clear the list
    twint.output.tweets_list = []

    # NEED TO CHANGE
    output_topic_tweet_count = open('user_Topic_tweet_Count_TEST.txt', 'w')
    # output_topic_tweet_count = open('user_Topic_tweet_Count_PREDICT.txt', 'w')
    userTopic_tweet_Dict_str = str(topic_tweet_Dict)
    output_topic_tweet_count.write(userTopic_tweet_Dict_str)
    output_topic_tweet_count.close()

    # NEED TO CHANGE
    output_topicNumber = open('user_TopicCount_TEST.txt', 'w')
    # output_topicNumber = open('user_TopicCount_PREDICT.txt', 'w')
    userTopicDict_str = str(userTopicDict)
    output_topicNumber.write(userTopicDict_str)
    output_topicNumber.close()

    # NEED TO CHANGE
    output_retweet = open('user_retweet_TEST.txt', 'w')
    # output_retweet = open('user_retweet_PREDICT.txt', 'w')
    user_retweetDict_str = str(userRetweetDict)
    output_retweet.write(user_retweetDict_str)
    output_retweet.close()












