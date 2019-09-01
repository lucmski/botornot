import csv

f1 = eval(open('./yanxiao/each_movie_TEST1.txt', 'r').read())
f2 = eval(open('./yanxiao/each_movie_TEST2.txt', 'r').read())
f3 = eval(open('./yanxiao/each_movie_TEST3.txt', 'r').read())
f4 = eval(open('./yanxiao/each_movie_TEST4.txt', 'r').read())
f5 = eval(open('./yanxiao/each_movie_TEST5.txt', 'r').read())
f6 = eval(open('./yanxiao/each_movie_TEST6.txt', 'r').read())
f7 = eval(open('./travis/each_movie_TEST1.txt', 'r').read())
f8 = eval(open('./travis/each_movie_TEST2.txt', 'r').read())
f9 = eval(open('./travis/each_movie_TEST3.txt', 'r').read())
f10 = eval(open('./travis/each_movie_TEST4.txt', 'r').read())
f11 = eval(open('./travis/each_movie_TEST5.txt', 'r').read())
f12 = eval(open('./travis/each_movie_TEST6.txt', 'r').read())
f13 = eval(open('./travis/each_movie_TEST7.txt', 'r').read())
f14 = eval(open('./travis/each_movie_TEST8.txt', 'r').read())
f15 = eval(open('./travis/each_movie_TEST.txt', 'r').read())

n1 = eval(open('./yanxiao/each_movie_PREDICT1.txt', 'r').read())
n2 = eval(open('./yanxiao/each_movie_PREDICT2.txt', 'r').read())
n3 = eval(open('./yanxiao/each_movie_PREDICT3.txt', 'r').read())
n4 = eval(open('./yanxiao/each_movie_PREDICT4.txt', 'r').read())
n5 = eval(open('./yanxiao/each_movie_PREDICT5.txt', 'r').read())
n6 = eval(open('./yanxiao/each_movie_PREDICT6.txt', 'r').read())
n7 = eval(open('./travis/each_movie_PREDICT1.txt', 'r').read())
n8 = eval(open('./travis/each_movie_PREDICT2.txt', 'r').read())
n9 = eval(open('./travis/each_movie_PREDICT3.txt', 'r').read())
n10 = eval(open('./travis/each_movie_PREDICT4.txt', 'r').read())
n11 = eval(open('./travis/each_movie_PREDICT5.txt', 'r').read())
n12 = eval(open('./travis/each_movie_PREDICT6.txt', 'r').read())
n13 = eval(open('./travis/each_movie_PREDICT7.txt', 'r').read())
n14 = eval(open('./travis/each_movie_PREDICT8.txt', 'r').read())


# 851
predict = []
# test 869
test = []


def jjj(l1, l2):
    for i in l1:
        l2.append(i)
    return l2

test = jjj(f1, test)
test = jjj(f2, test)
test = jjj(f3, test)
test = jjj(f4, test)
test = jjj(f5, test)
test = jjj(f6, test)
test = jjj(f7, test)
test = jjj(f8, test)
test = jjj(f9, test)
test = jjj(f10, test)
test = jjj(f11, test)
test = jjj(f12, test)
test = jjj(f13, test)
test = jjj(f14, test)
test = jjj(f15, test)


predict = jjj(n1, predict)
print(len(predict))
predict = jjj(n2, predict)
print(len(predict))
predict = jjj(n3, predict)
print(len(predict))
predict = jjj(n4, predict)
predict = jjj(n5, predict)
print(len(predict))
predict = jjj(n6, predict)
print(len(predict))
predict = jjj(n7, predict)
predict = jjj(n8, predict)
print(len(predict))
predict = jjj(n9, predict)
print(len(predict))
predict = jjj(n10, predict)
print(len(predict))
predict = jjj(n11, predict)
print(len(predict))
predict = jjj(n12, predict)
print(len(predict))
predict = jjj(n13, predict)
print(len(predict))
predict = jjj(n14, predict)
print(len(predict))

# print(predict)

print(len(f1))
print(len(f2))
print(len(f3))
print(len(f4))
print(len(f5))
print(len(f6))
print(len(f7))
print(len(f8))
print(len(f9))
print(len(f10))
print(len(f11))
print(len(f12))
print(len(f13))
print(len(f14))

print(len(predict))
print(len(test))
def export_predict(filename, list1):
    csv_columns = ['user', 'rojo', 'crawl', 'stuber', 'thefarewell', 'bethanyhamiton']
    try:
        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in list1:
                writer.writerow(data)
    except IOError:
        print("I/O error") 

def export_test(filename, list1):
    csv_columns = ['user', 'headCount', 'deepmurder', 'shaft', 'hampstead', 'vault']
    try:
        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in list1:
                writer.writerow(data)
    except IOError:
        print("I/O error") 

export_predict('./data/each_movie_PREDICT.csv', predict)
export_test('./data/each_movie_TEST.csv', test)





                     

 
