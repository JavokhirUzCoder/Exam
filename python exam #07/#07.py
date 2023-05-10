entered_list = input().split(" ")

result = []
result.append(entered_list[1:])
result.append(entered_list[0])
result = list(result)
print(result)
print("Success!")