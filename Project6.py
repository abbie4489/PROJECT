def integer_checker(question):
    error = "\nSorry, you must enter an integer\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


car_list = [(1, "Suzuki Van", 2), (2, "Toyota Corolla", 4),
                (3, "Honda CRV", 4), (4, "Suzuki Swift", 4),
                (5, "Mitsibishi Airtrek", 4), (6, "Nissan DC Ute", 4),
                (7, "Toyota Previa", 7), (8, "Toyota Hi Ace", 12),
                (9, "Toyota Hi Ace", 12)]
booked = []
valid = False
while not valid:
    seats_needed = integer_checker("How many seats do you need? ")
    if seats_needed == -1:
        for i in booked:
            print("Name:", i[0], " Car number:", i[1][0], " Car type:", i[1][1])
        valid = True
    else:
        for i in car_list:
            if i[2] < seats_needed:
                print(i[0], i[1], i[2], "--not enough space--")
            else:
                print(i[0], i[1], i[2])
        car = integer_checker("Enter vehicle number you would like:")
        name = input("Enter your name")
        for i in booked:
            print(i)
            if car == i[1][0]:
                print("already booked")
        for x in car_list:
            if x[0] == car:
                booked.append((name, car_list[car_list.index(x)][0:2]))
                del car_list[(car_list.index(x))]
