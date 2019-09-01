import csv
import networkx as nx

def export(filename, list1):
    with open(filename, mode = 'w') as csv_file:
        writer = csv.writer(csv_file)
        for i in list1:
            writer.writerow(i)

def dictSort(dict1):
    dict1 = sorted(dict1.items(), key = lambda x: x[0])
    return dict1


retweet_dict_TEST = dictSort(eval(open('./data/retweet_dict_TEST.txt', 'r').read()))
retweet_dict_PREDICT = dictSort(eval(open('./data/retweet_dict_PREDICT.txt', 'r').read()))
topic_tweets_count_TEST = dictSort(eval(open('./data/topic_tweets_dict_TEST.txt', 'r').read()))
topic_tweets_count_PREDICT = dictSort(eval(open('./data/topic_tweets_dict_PREDICT.txt', 'r').read()))
topic_keyword_count_TEST = dictSort(eval(open('./data/topic_keyword_dict_TEST.txt', 'r').read()))
topic_keyword_count_PREDICT = dictSort(eval(open('./data/topic_keyword_dict_PREDICT.txt', 'r').read()))
user_tweets_count_TEST = dictSort(eval(open('./data/userTweetsCount_TEST.txt', 'r').read()))
user_tweets_count_PREDICT = dictSort(eval(open('./data/userTweetsCount_PREDICT.txt', 'r').read()))

i_retweet_dict_TEST = [i[0] for i in retweet_dict_TEST]
i_retweet_dict_PREDICT = [i[0] for i in retweet_dict_PREDICT]
i_topic_tweets_count_TEST = [i[0] for i in topic_tweets_count_TEST]
i_topic_tweets_count_PREDICT = [i[0] for i in topic_tweets_count_PREDICT]
i_keyword_count_TEST = [i[0] for i in topic_keyword_count_TEST]
i_keyword_count_PREDICT = [i[0] for i in topic_keyword_count_PREDICT]
i_user_tweets_count_TEST = [i[0] for i in user_tweets_count_TEST]
i_user_tweets_count_PREDICT = [i[0] for i in user_tweets_count_PREDICT]

network_dict_TEST = eval(open('./data/network_TEST_DONE.txt', 'r').read())
network_dict_PREDICT = eval(open('./data/network_PREDICT_DONE.txt', 'r').read())

network_TEST = nx.DiGraph(network_dict_TEST)
network_PREDICT = nx.DiGraph(network_dict_PREDICT)

def getDiff(l1, l2):
    l3 = []
    for i in l1:
        if i not in l2:
            l3.append(i)
    return l3

def getTuple(l1, l2):
    l3 = []
    for i in l1:
        for j in l2:
            if j[0] == i:
                l3.append(j)
    return l3

def remove(toDelete, orig):
    for i in toDelete:
        orig.remove(i)
    return orig

len_retweet_TEST = len(i_retweet_dict_TEST)
len_retweet_PREDICT = len(i_retweet_dict_PREDICT)
len_topic_tweets_count_TEST = len(i_topic_tweets_count_TEST)
len_topic_tweets_count_PREDICT = len(i_topic_tweets_count_PREDICT)
len_keyword_TEST = len(i_keyword_count_TEST)
len_keyword_PREDICT = len(i_keyword_count_PREDICT)
len_user_tweets_TEST = len(i_user_tweets_count_TEST)
len_user_tweets_PREDICT = len(i_user_tweets_count_PREDICT)

print(len_retweet_TEST)
print(len_topic_tweets_count_TEST)
print(len_keyword_TEST)
print(len_user_tweets_TEST)
print()
print(len_retweet_PREDICT)
print(len_topic_tweets_count_PREDICT)
print(len_keyword_PREDICT) #
print(len_user_tweets_PREDICT)

j_retweet_dict_TEST = getDiff(i_retweet_dict_TEST, i_user_tweets_count_TEST)
j_topic_tweets_count_TEST = getDiff(i_topic_tweets_count_TEST, i_user_tweets_count_TEST)
j_keyword_count_TEST = getDiff(i_keyword_count_TEST, i_user_tweets_count_TEST)
j_user_tweets_count_TEST = getDiff(i_user_tweets_count_TEST, i_user_tweets_count_TEST)

j_keyword_count_PREDICT = getDiff(i_keyword_count_PREDICT, i_user_tweets_count_PREDICT)
j_retweet_dict_PREDICT = getDiff(i_retweet_dict_PREDICT, i_user_tweets_count_PREDICT)
j_topic_tweets_count_PREDICT = getDiff(i_topic_tweets_count_PREDICT, i_user_tweets_count_PREDICT)
j_user_tweets_count_PREDICT = getDiff(i_user_tweets_count_PREDICT, i_user_tweets_count_PREDICT)

to_delete_retweet_dict_TEST = getTuple(j_retweet_dict_TEST, retweet_dict_TEST) 
to_delete_retweet_dict_PREDICT = getTuple(j_retweet_dict_PREDICT, retweet_dict_PREDICT) 
to_delete_topic_tweets_count_TEST = getTuple(j_topic_tweets_count_TEST, topic_tweets_count_TEST)
to_delete_topic_tweets_count_PREDICT = getTuple(j_topic_tweets_count_PREDICT, topic_tweets_count_PREDICT)
to_delete_keyword_count_TEST = getTuple(j_keyword_count_TEST, topic_keyword_count_TEST)
to_delete_keyword_count_PREDICT = getTuple(j_keyword_count_PREDICT, topic_keyword_count_PREDICT)
to_delete_user_tweets_count_TEST = getTuple(j_user_tweets_count_TEST, user_tweets_count_TEST)
to_delete_user_tweets_count_PREDICT = getTuple(j_user_tweets_count_PREDICT, user_tweets_count_PREDICT)

print(j_retweet_dict_TEST)
print()
print()
print(to_delete_keyword_count_PREDICT)


retweet_dict_TEST = remove(to_delete_retweet_dict_TEST, retweet_dict_TEST)
retweet_dict_PREDICT = remove(to_delete_retweet_dict_PREDICT, retweet_dict_PREDICT)
topic_tweets_count_TEST = remove(to_delete_topic_tweets_count_TEST, topic_tweets_count_TEST)
topic_tweets_count_PREDICT = remove(to_delete_topic_tweets_count_PREDICT, topic_tweets_count_PREDICT)
topic_keyword_count_TEST = remove(to_delete_keyword_count_TEST, topic_keyword_count_TEST)
topic_keyword_count_PREDICT = remove(to_delete_keyword_count_PREDICT, topic_keyword_count_PREDICT)
user_tweets_count_TEST = remove(to_delete_user_tweets_count_TEST, user_tweets_count_TEST)
user_tweets_count_PREDICT = remove(to_delete_user_tweets_count_PREDICT, user_tweets_count_PREDICT)




network_remove_PREDICT = []
network_remove_TEST = []
for i in network_TEST:
    if i not in i_user_tweets_count_TEST:
        network_remove_TEST.append(i)

for i in network_PREDICT:
    if i not in i_user_tweets_count_PREDICT:
        network_remove_PREDICT.append(i)

network_TEST.remove_nodes_from(network_remove_TEST)
network_PREDICT.remove_nodes_from(network_remove_PREDICT)





out_retweet_dict_TEST = export('retweet_count_TEST.csv', retweet_dict_TEST)
out_retweet_dict_PREDICT = export('retweet_count_PREDICT.csv', retweet_dict_PREDICT)
out_TopicCount_dict_TEST = export('tweets_keyword_count_TEST.csv', topic_keyword_count_TEST) 
out_TopicCount_dict_PREDICT = export('tweets_keyword_count_PREDICT.csv', topic_keyword_count_PREDICT) 
out_topic_tweets_count_TEST = export('topic_tweets_count_TEST.csv', topic_tweets_count_TEST)
out_topic_tweets_count_PREDICT = export('topic_tweets_count_PREDICT.csv', topic_tweets_count_PREDICT)
out_user_tweets_count_TEST = export('user_tweets_count_TEST.csv', user_tweets_count_TEST)
out_user_tweets_count_PREDICT = export('user_tweets_count_PREDICT.csv', user_tweets_count_PREDICT)



out_network_TEST = open('./data/network_TEST_DONE1.txt', 'w')
out_network_PREDICT = open('./data/network_PREDICT_DONE1.txt', 'w')
out_network_TEST.write(str(nx.to_dict_of_dicts(network_TEST)))
out_network_PREDICT.write(str(nx.to_dict_of_dicts(network_PREDICT)))
out_network_TEST.close()
out_network_PREDICT.close()




