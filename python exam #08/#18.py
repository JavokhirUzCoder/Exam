UpperCase = "QWERTYUIOPASDFGHJKLZXCVBNM"
LowerCase = "qwertyuiopasdfghjklzxcvbnm"
Symbols = "!@#$%^&*<>"
Numbers = "1234567890"


def IsTrue(password):
    isUpper = False
    isLower = False
    isSymbol = False
    isNumber = False
    if len(password) >=6 and len(password) <= 12:
        for i in password:
            if i in UpperCase:
                isUpper = True
            if i in LowerCase:
                isLower = True
            if i in Symbols:
                isSymbol= True
            if i in Numbers:
                isNumber = True
        if isUpper and isLower and isNumber and isSymbol:
            return True
        else:
            return False
    else:
        return False



Password = input().split(",")

for i in Password:
    if IsTrue(i):
        print(i, end = " ")

