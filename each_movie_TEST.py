import networkx as nx
import twint


f = open('./data/network_TEST_DONE.txt', 'r')
# f = open('./data/network_PREDICT_DONE.txt', 'r')
userDict = eval(f.read())
userGraph = nx.DiGraph(userDict)

userList = list(userGraph.nodes)
userList.sort()

def export(filename, list1):
    csv_columns = ['user', 'headCount', 'deepmurder', 'shaft', 'hampstead', 'vault']
    try:
        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError:
        print("I/O error") 


# NEED TO CHANGE
userList = [userList[i] for i in range(865, 869)]

l1 = []

for user in userList:
    
    print(user)
    userDict = {}
    userDict["user"] = user

    c1 = twint.Config()
    c1.Username = user
    c1.Store_object = True
    c1.Search = "#headCount"
    twint.run.Search(c1)
    userDict["headCount"] = len(twint.output.tweets_list)

    twint.output.tweets_list = []

    c2 = twint.Config()
    c2.Username = user
    c2.Store_object = True
    c2.Search = "#deepmurder"
    twint.run.Search(c2)
    userDict["deepmurder"] = len(twint.output.tweets_list)

    twint.output.tweets_list = []
    
    c3 = twint.Config()
    c3.Username = user
    c3.Store_object = True
    c3.Search = "#shaft"
    twint.run.Search(c3)
    userDict["shaft"] = len(twint.output.tweets_list)

    twint.output.tweets_list = []

    c4 = twint.Config()
    c4.Username = user
    c4.Store_object = True
    c4.Search = "#hampstead"
    twint.run.Search(c4)
    userDict["hampstead"] = len(twint.output.tweets_list)

    twint.output.tweets_list = []

    c5 = twint.Config()
    c5.Username = user
    c5.Store_object = True
    c5.Search = "#vault"
    twint.run.Search(c5)
    userDict["vault"] = len(twint.output.tweets_list)

    twint.output.tweets_list = []

    l1.append(userDict)
    print(l1)


    output = open('each_movie_TEST.txt', 'w')
    output.write(str(l1))
    output.close()
    
output = open('each_movie_TEST.txt', 'w')
output.write(str(l1))
output.close()

print("COMPLETE")








