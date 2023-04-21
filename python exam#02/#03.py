email = input("Email kiritib ko`ringchi:  ")

trueEmailSymbol = "@"

trueEmailSymbol2 = ".com"

if email == email.lower() and trueEmailSymbol in email and trueEmailSymbol2 in email:
    print("Yes, This email is valid")
else:
    print("No, This email is invalid")
