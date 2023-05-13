nums = input().split(',')
result = []

for i in nums:
    if  int(i)%2==1:
        result.append(i)


print("" + ','.join(result))
