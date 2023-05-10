# Fibonachi sonlari yig`indisi
fibbo = [1,1]
i = 1
x = int(input())


while (fibbo[i] <= x):
    fibbo.append(fibbo[i]+fibbo[i-1])
    i += 1

print(sum(fibbo[0:-1]))