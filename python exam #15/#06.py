file = open("input6.txt", "w+")
file.write(input())
file.close()
file = open("input6.txt", "r")
num = int(file.read())
file.close()

file = open("output6.txt", "w+")


if num % 2==0:
    file.write("Juft")
else:
    file.write("Toq")

file.close()