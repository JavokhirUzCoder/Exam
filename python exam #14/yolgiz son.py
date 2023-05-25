Numofcount = int(input())
Numbers = list(map(int, input().split(' ')))
if Numofcount !=1:
    Numbers.sort()

    Newcounter = [0 for i in range(Numofcount)]

    k=0
    for i in Numbers:
        for j in Numbers:
            if i == j:
                Newcounter[k] +=1
        k+=1
else:
    Numbers[0]

if 1 in Newcounter:
    print(Numbers[Newcounter.index(1)])


file = open("input.txt", "w+")
file.write(f'{Numbers}')
file.close()

file = open("output.txt", "w+")
file.write(f'{Numbers[Newcounter.index(1)]}')
file.close()