import os
from random import *

file = open("base.txt" , "w+")
file.close()
number = [1,2,3,4,5,6,7,8,9,0]
LocalList =[]
while True:
    def Generate():
        Company = int(input("Company >>> "))
        Count = int(input("Count >>> "))
        for i in range(Count):
            
            # Main place
            
            tel = ""
            for k in range(7):
                tel += str(choice(number))
            tel = str(Company) + tel
            
            # Main place
            
            with open("base.txt", "a") as file:
                x = tel
                LocalList.append(x)
                file.write(x[:2]+ " "+ x[2:5] + " " + x[5:7] + " "  + x[7:] + "\n")
        os.system("cls")
        print("\nGenerating Success")

    def ViewList():
        os.system("cls")
        with open("base.txt", "r") as file:
            listPhone = file.read().split("\n")
        listPhone = listPhone[:-1]
        for i in listPhone:
            print(f"({listPhone.index(i)+1}) => {i}")

    def Add():
        phone  = input("Enter (with spaces in between => (00 000 00 00) )>>> ")
        isPNum = 0
        for i in phone:
            if i.isdigit():
                isPNum += 1
        if isPNum == 9: 
            with open("base.txt", "a") as file:
                file.write(phone+ "\n")
                print("\n"+ phone +" Add successfully \n")
        else:
            print("\nSomething went wrong\n")
            Add()


    def Remove():
        os.system("cls")
        ViewList()
        Item = input("\nItem: ")
        with open("base.txt", "r") as file:
            listPhone = file.read().split("\n")
            listPhone = listPhone[:-1]
        if input("Is it clear? (y/n): ").lower() == "y":
            if Item.isdigit():
                try:
                    del listPhone[int(Item)-1]
                    with open("base.txt", "w+") as reFile:
                        reFile.write("\n".join(listPhone)+"\n")
                except :
                    print("Something went wrong")
                    Remove()
                else:
                    print("\nRemove Successfully \n")
            else:
                isPNum = 0
                for i in Item:
                    if i.isdigit():
                        isPNum += 1
                if isPNum == 9:
                    try:
                        listPhone.remove(Item)
                        with open("base.txt", "w+") as reFile:
                            reFile.write("\n".join(listPhone)+"\n")
                    except:
                        print("Remove failed")
                    else:
                        print("\nRemove Successfully \n")
                else:
                    print("\nRemove Failed\n")
                    Remove()
        else:
            print("\nRemove cancelled\n")

    def Command():
        x = input("\n(1) Generate\n(2) View List \n(3) Add\n(4) Remove\n(5) Exit\nComand: ")
        if  x == "1":
            Generate()
        elif x == "2":
            ViewList()
        elif x == "3":
            Add()
        elif x == "4":
            Remove()
        elif x == "5":
            os.system("cls")
            exit()
        else:
            Command()
    Command()