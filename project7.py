# Mikael Hinton
# Project 7
# iRand from Project 5
# InsertionSort from Project 6 https://www.geeksforgeeks.org/insertion-sort/
# BinarySearch https://stackoverflow.com/questions/38346013/binary-search-in-a-python-list

# irand is a function given to the students that generates a list of length
# is the random selection of the integers from 0 to 1-m without replacement
def irand(n,m): # generate an array of length n made up of random integers
    import random # between 0 and m without replacement
    b = list(range(n))
    b = random.sample(range(m), n)
    return b

A = irand(100, 200)

def insertionSort(arr):
    for i in range(1, len(arr)):
        k =arr[i]
        j = i -1
        while j >=0 and k < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = k

insertionSort(A)

print("InsertionSort ==", A)

# if the number if found then then it prints out the number and position
# if the number if not found and the f is less than or equal to the length of the list then if keeps searching and either incrementing the
#   midpoint up or down by 1 if the number is more or less than the midpoint until its either found or it runs out of number and then 
#   will print that the number is not in the sequence
def binarySearch(list, number):
    f = 0
    l = len(list)-1
    found = False

    while f<=l and not found:
        pos = 0
        midpoint = (f + l)//2
        if list[midpoint] == number:
            pos = midpoint
            found = True
            print( number, "is in position", pos)
        else:
            if number < list[midpoint]:
                l = midpoint-1
            else:
                f = midpoint+1
    if found == False:
        print(number, "is not in the sequence")

num = input("What number would you like to search for?\n")
convertedNum = int(num)
print("You have chosen to search for: ", convertedNum)
binarySearch(A, convertedNum)
