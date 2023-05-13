word = input()

Upperletters = 0
Lowerletters = 0

for i in word:
    if i.lower() == i:
        Lowerletters += 1
    if i.upper() == i:
        Upperletters += 1
        
print("UPPERCASE: " , Upperletters)
print("lOWERCASE: " ,Lowerletters)