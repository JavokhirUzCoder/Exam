# Sonlar takrorlanmasligi


def func(a):
    for i in range(1,a+1):
        x = [i//1000, i//100%10, i//10%10, i%10]
        if (x[0] != x[1]) and (x[1] != x[2]) and (x[1] != x[2]) and (x[2] != x[3]) and (x[3] != x[0]) and (x[0] != x[1]) and  (x[2] != x[0])  and (x[1] != x[3]):
            if (x[0] == 0):
                print(f"{x[1]}{x[2]}{x[3]}")
                if (x[1] == 0):
                    print(f"{x[2]}{x[3]}")
                if (x[2] == 0):
                    print(f"{x[3]}")
            else:
                print(f"{x[0]}{x[1]}{x[2]}{x[3]}")
            

func(int(input()))