balance = 0
while True:
    line = input()
    if line:
        if line[0].lower() == "d":
            balance += int(line[2:])
        if line[0].lower() == "w":
            balance -= int(line[2:])   
    else:
        break

print(balance)