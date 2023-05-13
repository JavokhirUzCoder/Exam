result = []
isJuft = True
nums = input().split(",")
for i in nums:
    for j in i:
        if int(j)%2==1:
            isJuft = False
            break
    if isJuft:
        result.append((i))
        
print("" + ','.join(result))
