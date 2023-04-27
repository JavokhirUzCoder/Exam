# Sonlar haqida 
import math


def isPrime(num):
    if(num==1) and (num %2 ==0):
        return False
    if(num==2):
        return True

    i = 3
    while(i<math.sqrt(num)+1):
        if num%i==0:
            return False
        i += 2
    return True

num = int(input("Enter number: "))

if num < 0:
    print("Son manfiy")
elif num == 0:
    print("Son nolga teng")
else:
    if num % 2 == 0:
        print("Son musbat juft son")
    else:
        print("Son musbat toq son")


if input("Siz kiritgan raqam tub ekanligini tekshirishni xoxlaysizmi (Ha / Yo`q): ").lower() == "ha":
    if isPrime(num):
        print("Siz kiritgan son tub son")
    else:
        print("Afsuski, Siz kiritgan son tub emas")