# Integer checking function - loops until a valid number is entered

def integer_checker(question):
    error = "\nSorry, you must enter an integer\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


speeds_list = []
criminals = ["James Wilson", "Helga Norman", "Zachary Conroy"]
price = []
vaild = False
while not vaild:
    print("------------------------------")
    name = input("Enter the name of the speeder: ").title()
    if name in criminals:
        print(name.upper(), "WARRANT TO ARREST")
    elif name == "X":
        total_fines = len(speeds_list)
        print(f"Total Fines: {total_fines}")
        for position in speeds_list:
            print("Name:", position[0], "   Amount over limit:", position[1])
        print("Total amount of fines", sum(price))
        break
    speed = integer_checker("Enter the amount over the speed limit: ")
    if speed < 10:
        price.append(10)
    elif 10 <= speed <= 14:
        price.append(80)
    elif 15 <= speed <= 19:
        price.append(120)
    elif 20 <= speed <= 24:
        price.append(170)
    elif 25 <= speed <= 29:
        price.append(230)
    elif 30 <= speed <= 34:
        price.append(300)
    elif 35 <= speed <= 39:
        price.append(400)
    elif 40 <= speed <= 44:
        price.append(510)
    else:
        price = 630
    speeds_info = (name, speed)
    speeds_list.append(speeds_info)
    print(f"{name} is to be fined ${price}")
    print("------------------------------")

