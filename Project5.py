# Mikael Hinton
# Project 5 
# Functions from Project 5 

# irand is a function given to the students that generates a list of length
# is the random selection of the integers from 0 to 1-m without replacement
def irand(n,m): # generate an array of length n made up of random integers
    import random # between 0 and m without replacement
    b = list(range(n))
    b = random.sample(range(m), n)
    return b

A = irand(100, 200)
B = irand(100,200)

A.sort()
B.sort()

# A intersect B
# If the # in A and # in B are equal then it appends it to the new []
def intersect(a,b):
    inter = []
    for i in A:
        for j in B:
            if i==j:
                inter.append(i)
    return inter
print("")
print("INTERSECT")
print(intersect(A,B))
print("")
print("List A:",A)
print("")
print("List B:",B)

# A-B
# if the # in A then it appends it to []
# if the # is in A and B then it doesnt include it in the []
def AminB(a,b):
    AmB = []
    for i in a:
        t = True
        for j in b:
            if i == j:
                t=False
                break
        if t :
            AmB.append(i)
    return AmB
print("")
print("A MINUS B")
print(AminB(A,B))
print("")
print("List A:",A)
print("")
print("List B:",B)

# A union B
# if # is in B then append to [] and then if the # is in A and not in B then it appends it to [] and then sorts []
def union(a,b):
    u = []
    for i in b:
        u.append(i)
    for j in AminB(a,b):
        u.append(j)
    u.sort()
    return u
print("")
print("UNION")
print(union(A,B))
print("")
print("List A:",A)
print("")
print("List B:",B)

# Not A given a universal set
# Takes in universal set and it does univeral set minus A and returns what is not in A given Universal Set
Universal = list(range(200))
def compliment(u,a):
    return AminB(u,a)
print("")
print("COMPLIMENT")
print(compliment(Universal,A))
print("")
print("List A:",A)


# A XOR B
# Appends what A minus B to [] and then appends B minus A to [] and then sorts
def xor(a,b):
    axb = []
    for i in AminB(a,b):
        axb.append(i)
    for j in AminB(b,a):
        axb.append(j)
    axb.sort()
    return axb
print("")
print("XOR")
print(xor(A,B))
print("")
print("List A:",A)
print("")
print("List B:",B)