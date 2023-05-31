import os
from random import *

score = 5

Values = ["a", "b", "c"]

os.system("cls")
while True:
    print("""
    |--------------------------|
    |                          |
    |         |------|         |
    |         |   A  |         |
    |         |______|         |
    |                          |
    |                          |
    |         |------|         |
    |         |   B  |         |
    |         |______|         |
    |                          |
    |                          |
    |         |------|         |
    |         |   C  |         |
    |         |______|         |
    |                          |
    |__________________________|""")
    print(f"Your score is {score}")
    Select = choice(Values)
    User = input("Select the box, which you want: ").lower()
    if User == Select:
        score += 1
        print(f"Correct👍, Your score is {score}")
    else:
        score -= 1
        print(f"Incorrect👎 ,Your score is {score}")
    if score == 0:
        print("Game over")
        break
print("The End")