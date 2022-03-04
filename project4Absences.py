"""Project 4 - Absences at work
this program is designed to record data about the absences at work
abbie
"""

# Integer checking function - loops until a valid number is entered

def integer_checker(question):
    error = "\nSorry, you must enter an integer\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            round(number)
            return number
        except ValueError:
            print(error)


# main routine
name_list = []
highest_absence = 0
highest_absence_name = ""
count = 0
total_absence = 0
not_absent = []
valid = False
while not valid:  # loops questions
    names = input("what is the name of the employer? ")
    if names != "$":
        count += 1
        absence = integer_checker("how many absence days have they had?")
        total_absence += absence  # sums the amount of absences
        employees = (names, absence)
        name_list.append(employees)  # adds names to the list
        if absence > highest_absence:  # if the absence is greater than the previous highest absence
            highest_absence = absence  # changes the amount of days
            highest_absence_name = names  # changes the name of the highest absence
        elif absence == 0:  # if employee had no absences
            not_absent.append(names)  # adds it to list called not_absent
            not_absent.sort()  # sorts names alphabetically
    if names == "$":  # breaks the loop
        average_absence = round(total_absence / count, 2)  # works out average and rounds it to 2dp
        name_list.sort()  # sorts alphabetically
        # printing results
        print(f"Average number of absence days:\n{average_absence}")
        print(f"The person with the most absence days:\n{highest_absence_name}"
              f" with {highest_absence} days")
        print("List of people not absent at all:", *not_absent, sep="\n")  # takes the brackets of the list
        print("List of people absent above average:")
        employees_over = []  # a list for employees over the average
        for employ in name_list:
            if employ[1] > average_absence:  # if position absence days is over the average
                employees_over.append(employ)  # adds it to the list for employees over the average
        for position in employees_over:
            print(position[0], position[1])  # printing the list of employees over
        break
