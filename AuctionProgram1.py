"""Programming Project #2
The task is to design and write a program which takes care of a silent auction.
Abbie
"""


def float_checker(question):   # function to check if input is float
    error = "\nSorry, you must enter an integer\n"
    number = ""
    while not number:  # if its not float
        try:
            number = float(input(question))
            return number
        except ValueError:
            print(error)


#  main code
print("Welcome to the auction press -1 to finish auction\n")
bid_list = [0]
bid = 0
item = input("what is the auction for?")
reserve = float_checker("what is the reserve price?")
round(reserve, 2)
print("the auction for the", item, "has started!!")
print("--------------------------------------------")
vaild = False
while not vaild:  # creating loop
    highest_bid = max(bid_list)  # variable is the highest number in list
    print("\nthe highest bid so far is", highest_bid)
    bid1 = float_checker("what is your bid?")
    bid = round(bid1, 2)  # rounding to 2 dp
    bid_list.append(bid)  # adding bid to list
    if bid != -1:
        if bid < highest_bid:
            print("please enter a higher bid")
    elif bid == -1:  # to finish bid
        if highest_bid > reserve:  # bid is greater than reserve price
            print("-------------------------------------------------------")
            print("the auction for the", item, "has finished with a bid of",
                  highest_bid)
            print("-------------------------------------------------------")
            break  # ends program
        elif highest_bid < reserve:  # bid is less than reserve price
            print("---\nsorry this item cannot be sold as it did not meet the"
                  " reserve price\n---")
            break  # ends program
