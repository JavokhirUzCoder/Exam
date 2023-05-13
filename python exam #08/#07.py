x = int(input())
y = int(input())


m = 0
result = []

for i in range(x):
    for s in range(y):
        result[m] = list()
        result[int(i)].append(m)
    m+=1


print(result)
        