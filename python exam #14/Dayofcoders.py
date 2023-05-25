def Dayofcoder(year):
    if year % 4 == 0:
        return f"12/09{year}"
    else:
        return f"13/09{year}"

x = int(input())
print(Dayofcoder(x))


file = open("input.txt", "w+")
file.write(f'{x}')
file.close()

file = open("output.txt", "w+")
file.write(f'{Dayofcoder(x)}')
file.close()