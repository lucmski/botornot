import networkx as nx
import twint


# f = open('./data/network_TEST_DONE.txt', 'r')
f = open('./data/network_PREDICT_DONE.txt', 'r')
userDict = eval(f.read())
userGraph = nx.DiGraph(userDict)

userList = list(userGraph.nodes)
userList.sort()

def export(filename, list1):
    csv_columns = ['user', 'rojo', 'crawl', 'stuber', 'thefarewell', 'bethanyhamiton']
    try:
        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError:
        print("I/O error") 


# NEED TO CHANGE
userList = [userList[i] for i in range(480, 500)]

l1 = []

for user in userList:
    
    print(user)
    userDict = {}
    userDict["user"] = user

    c1 = twint.Config()
    c1.Username = user
    c1.Store_object = True
    c1.Search = "#rojo"
    twint.run.Search(c1)
    userDict["rojo"] = len(twint.output.tweets_list)

    twint.output.tweets_list = []

    c2 = twint.Config()
    c2.Username = user
    c2.Store_object = True
    c2.Search = "#crawl"
    twint.run.Search(c2)
    userDict["crawl"] = len(twint.output.tweets_list)

    twint.output.tweets_list = []
    
    c3 = twint.Config()
    c3.Username = user
    c3.Store_object = True
    c3.Search = "#stuber"
    twint.run.Search(c3)
    userDict["stuber"] = len(twint.output.tweets_list)

    twint.output.tweets_list = []

    c4 = twint.Config()
    c4.Username = user
    c4.Store_object = True
    c4.Search = "#thefarewell"
    twint.run.Search(c4)
    userDict["thefarewell"] = len(twint.output.tweets_list)

    twint.output.tweets_list = []

    c5 = twint.Config()
    c5.Username = user
    c5.Store_object = True
    c5.Search = "#bethanyhamiton"
    twint.run.Search(c5)
    userDict["bethanyhamiton"] = len(twint.output.tweets_list)

    twint.output.tweets_list = []

    l1.append(userDict)
    print(l1)

    output = open('each_movie_PREDICT1.txt', 'w')
    output.write(str(l1))
    output.close()
    
output = open('each_movie_PREDICT1.txt', 'w')
output.write(str(l1))
output.close()

print("COMPLETE")







