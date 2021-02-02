# Mikael Hinton
# getSym(x) was taken from this website: https://stackoverflow.com/questions/57862191/python-programming-truth-table

def getSym(x):
    if x:
        return '| True '
    else:
        return '| False'



values = [True, False]
print(" ---------------------------------------------------------------")
print("|   P  ", "|   Q  ", "|  P^Q ", "| N(P^Q)|", "  NP  |","  NQ  |", "NPvNQ |", " iff  |")
print(" ---------------------------------------------------------------")
for p in values:
    for q in values:
        print(getSym(p), getSym(q), getSym(p and q), getSym(not (p and q)), getSym(not (p)), getSym(not (q)), getSym((not p) or (not q)), getSym(not p or q and not q or p), "|")
        print(" ---------------------------------------------------------------")


