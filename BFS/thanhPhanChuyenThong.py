def bfs(ele,data):
    


data='''1 2
2 3
2 4
3 6
3 7
6 7
5 8
8 9
'''
dictionary={i:[] for i in set(data.replace('\n',' ').split(' ')[:-2])}
data=data.split('\n')[:-2]

for i in data:
    dictionary[i[0]].append(i[-1])


print(dictionary)
# print(data)