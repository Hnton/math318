# Mikael Hinton
# Project 3
# getValue(x) was taken from this website: https://stackoverflow.com/questions/57862191/python-programming-truth-table


# Function that if returns the values of either true or false 
def getValue(x):
    if x:
        return '| True '
    else:
        return '| False'


# Values of the truth table
values = [True, False]
# Prints the table and calls the getValue function to get either true or false
print(" ---------------------------------------------------------------")
print("|   P  ", "|   Q  ", "|  P^Q ", "| N(P^Q)|", "  NP  |","  NQ  |", "NPvNQ |", " iff  |")
print(" ---------------------------------------------------------------")
for p in values:
    for q in values:
        print(getValue(p), getValue(q), getValue(p and q), getValue(not (p and q)), getValue(not (p)), getValue(not (q)), getValue((not p) or (not q)), getValue(not p or q and not q or p), "|")
        print(" ---------------------------------------------------------------")


