listofNum = list(map(int,input().split(" ")))
listofNum.sort()
print(sum(listofNum[:4]), sum(listofNum[-4::]))




file = open("input.txt", "w+")
file.write(f'{listofNum}')
file.close()

file = open("output.txt", "w+")
file.write(f'{sum(listofNum[:4]), sum(listofNum[-4::])}')
file.close()