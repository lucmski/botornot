import twint
import networkx as nx

f = open('testUsers.txt', 'r')
# f = open('predictUser.txt', 'r')

# get the user graph from the txt
userStr = f.read()
userDict = eval(userStr)
userGraph = nx.DiGraph(userDict)

print("Nodes number: %d" % (userGraph.number_of_nodes()))
print("Edges number: %d" % (userGraph.number_of_edges()))

userList = list(userGraph.nodes)
userList.sort()

userList1 = [userList[i] for i in range(0, 100)]

count = 0
for user in userList1:
    c = twint.Config()
    c.Username = user
    c.Store_object = True
    print("user %s 's followings:" % (user))
    twint.run.Following(c)

    followings = twint.output.follows_list

    intersection = [user for user in userList1 if user in followings]
    for i in intersection:
        userGraph.add_edge(i, user)

    # clear the list
    twint.output.follows_list = []

    output = nx.to_dict_of_dicts(userGraph)
    strOutput = str(output)
    f = open('testUserDONE.txt', 'w')
    f.write(strOutput)
    f.close()

    edgeListOutput = str(list(userGraph.edges))
    edgeListFile = open('userEdgeList.txt', 'w')
    edgeListFile.write(edgeListOutput)
    edgeListFile.close()

    print("File saved")

print("ADD Complete")

# save the graph to txt
output = nx.to_dict_of_dicts(userGraph)
strOutput = str(output)
f = open('testUserDONE.txt', 'w')
f.write(strOutput)
f.close()

edgeListOutput = str(list(userGraph.edges))
edgeListFile = open('userEdgeList.txt', 'w')
edgeListFile.write(edgeListOutput)
edgeListFile.close()

print("SAVE complete")


