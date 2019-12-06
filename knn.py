from math import sqrt


def distance(point1, point2):
    return sqrt((point1[0] - float(point2[0])) ** 2 + (point1[1] - float(point2[1])) ** 2 + (point1[2] - float(point2[2])) ** 2 +(point1[3] - float(point2[3])) ** 2)


d = {}
with open('knn.text', 'r') as fhin:
    for line in fhin:
        words = line.strip().split(',')
        en_word = words.pop(4)
        # word=(words.pop(0),words.pop(0),words.pop(0),words.pop(0))
        d[tuple(words)] = en_word
v1,v2,v3,v4=float(input("1st value: ")),float(input("2nd value: ")),float(input("3rd value: ")),float(input("4th value: "))
k=int(input("Number of nearest neighbour: "))
point=(v1,v2,v3,v4)
d2={}
for key in d:
    print(key)
    # print(value)
    d2[distance(point,key)]=d[key]

results=[]
count=0
for i in sorted(d2):
    if count<k:
        results.append(d2[i])
    count+=1
print(results)