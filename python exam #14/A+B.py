x, y = map(int, input().split(" "))
print(x + y)


file = open("input.txt", "w+")
file.write(f'{str(x)} {str(y)}')
file.close()

file = open("output.txt", "w+")
file.write(f'{x + y}')
file.close()