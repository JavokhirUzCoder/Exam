email = input("Email kiritib ko`ringchi:  ")

trueEmailSymbol = "@"
trueEmailMust = ".com"

trueEmailSymbolReal = True
DoNotUse = ["!", "#", "$", "%", "^", "&", "*", "(", ")", "+","-","/",","]
for i in DoNotUse:
    if i in email:
        trueEmailSymbolReal = False

if email == email.lower() and (trueEmailSymbol in email) and (trueEmailMust in email) and trueEmailSymbolReal:
    print("Yes, This email is valid")
else:
    print("No, This email is invalid")
