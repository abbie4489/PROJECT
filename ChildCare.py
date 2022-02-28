"""This program is designed to be used by a child day center and keep track
of the children throughout the day
Abbie
"""

def main(choice):
    if choice != 5:
        print("------------------------------------------------------------")
        print("Welcome to MGS Childcare\nWhat would you like to do? Please "
              "choose one of the items below")
        print("------------------------------------------------------------\n")
        print(" 1 Drop off a child\n 2 pick up a child\n 3 calculate cost\n "
              "4 print roll\n 5 Exit the system\n")
    return choice


def dropOff(name_list):
    name = input("what child would you like to drop off?")
    name_list.append(name)
    print("the name", name, "has been added to the list")


def pickUp(name_list):
    vaild = False
    while not vaild:
        child_name = input("What child would you like to pickup?")
        remove_name = name_list.index(child_name)
        if child_name in name_list:
            name_list.pop(remove_name)
            print(name_list)
            return
        elif child_name not in name_list:
            print("the child is not in the list")


def calcCost():
    hours = integer_checker("how many hours has your child been here?")
    price = hours*12
    print("You have been charged", price)


def printRoll(name_list):
    print("\nthe names on the list are:", name_list)


def integer_checker(question):
    error = "\nSorry, you must enter a whole number between 1 and 4\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


# main routine
choice = 0
name_list = []
main(choice)
while choice != 5:
    choice = integer_checker("Enter your choice (number between 1 and 5): ")
    if choice == 1:
        dropOff(name_list)
    elif choice == 2:
        pickUp(name_list)
    elif choice == 3:
        calcCost()
    elif choice == 4:
        printRoll(name_list)
    else:
        print("Goodbye")
