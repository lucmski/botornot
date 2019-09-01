import networkx as nx
import csv

network_dict_TEST = eval(open('./data/network_TEST_DONE1.txt', 'r').read())
network_dict_PREDICT = eval(open('./data/network_PREDICT_DONE1.txt', 'r').read())

network_TEST = nx.DiGraph(network_dict_TEST)
network_PREDICT = nx.DiGraph(network_dict_PREDICT)


# 869
print(len(network_TEST.nodes))
#851
print(len(network_PREDICT.nodes))

adjacency_TEST = [[0 for i in range(0, 869)] for i in range(0, 869) ]
adjacency_PREDICT = [[0 for i in range(0, 851)] for i in range(0, 851)]

nodes_TEST = list(network_TEST.nodes)
nodes_TEST.sort()
nodes_PREDICT = list(network_PREDICT.nodes)
nodes_PREDICT.sort()

for i in nodes_TEST:
    for j in nodes_TEST:
        if network_TEST.has_edge(i, j):
            i_index = nodes_TEST.index(i)
            j_index = nodes_TEST.index(j)
            adjacency_TEST[i_index][j_index] = 1

for i in nodes_PREDICT:
    for j in nodes_PREDICT:
        if network_PREDICT.has_edge(i, j):
            i_index = nodes_PREDICT.index(i)
            j_index = nodes_PREDICT.index(j)
            adjacency_PREDICT[i_index][j_index] = 1

def export(filename, list1):
    with open(filename, mode = 'w') as csv_file:
        writer = csv.writer(csv_file)
        for i in list1:
            writer.writerow(i)

export('adjacency_TEST.csv', adjacency_TEST)
export('adjacency_PREDICT.csv', adjacency_PREDICT)


