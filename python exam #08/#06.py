def exam(l):
    q = (2*50*l)/30
    return (q)


x = input().split(",")


for i in x:
    print(exam(int(i)),end = ",")