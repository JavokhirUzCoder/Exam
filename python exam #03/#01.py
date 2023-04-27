age = int(input("Son kiriting: "))

text = "I think:  "

if age > 10 and age <= 19:
    print(text + "you are student of the school")
elif age > 18 and age <= 22:
    print(text + "you are student of the university")
elif age > 21 and age <= 40:
    print(text + "you are worker")
elif age > 40 and age <= 50:
    print(text + "you are boss of the other company")
elif age > 50 and age <= 70:
    print(text + "you are pensioner of the other company")
elif age > 70:
    print(text + "you are dead")
else:
    print(text + "you are none in the world")