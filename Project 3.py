"""Programming Project #3
Write a program which keep track of details for a taxi. The program should
start off by asking for the driver’s name. It should then repeatedly ask to
start a new trip.
Abbie
"""


def float_checker(question):  # checks the float and replies with error message
    error = "\nSorry, you must enter an integer\n"
    number = ""
    while not number:
        try:
            num = float(input(question))
            number = round(num, 2)  # rounds the num to 2 decimal places
            return number
        except ValueError:
            print(error)


# MAIN ROUTINE
cost = 0
cost_list = []
name = input("what is your name?")
vaild = False
while not vaild:  # loops
    trip = input("would you like to start a new trip y/n? ").upper()
    if trip == "Y":
        time = float_checker("how long was the trip? ")
        total_time = + time
        count = + 1
        cost = time*10 + 2
        cost_list.append(cost)
        print("the cost is", cost)
    if trip == "N":
        if cost > 1:
            print("\nthe drivers name:", name, "\ntotal time:", total_time, "\naverage time of all trips:", total_time / count,
                  "\nTotal income:", sum(cost_list), "\naverage cost for all trips:", sum(cost_list) / count)
            break
        if cost < 1:
            print("you need to enter a higher number than 1")


