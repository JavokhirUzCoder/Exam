listofNum = list(map(int,input().split(" ")))
listofNum.sort()
print(sum(listofNum[:4]), sum(listofNum[-4::]))