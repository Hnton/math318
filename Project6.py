# Mikael Hinton
# Project 6
# Functions from Project 6 https://www.geeksforgeeks.org/insertion-sort/

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

print("==========================================================================================================================================================================================================================")
print("Original == ",A)
print("==========================================================================================================================================================================================================================")
print("")
insertionSort(A)
print("==========================================================================================================================================================================================================================")
print("InsertionSort == ",A)
print("==========================================================================================================================================================================================================================")