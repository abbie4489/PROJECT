# Program to check if a Python list contains elements of another list

def list_contains(List1, List2):
    check = False

    # Iterate in the 1st list
    for m in List1:

        # Iterate in the 2nd list
        for n in List2:

            # if there is a match
            if m == n:
                check = True
                return check

    return check


# Test Case 1
List1 = ['a', 'e', 'i', 'o', 'u']
List2 = ['x', 'y', 'z', 'l', 'm']
print("Test Case#1 ", list_contains(List1, List2))

# Test Case 2
List1 = ['a', 'e', 'i', 'o', 'u']
List2 = ['a', 'b', 'c', 'd', 'e']
print("Test Case#2 ", list_contains(List1, List2))
