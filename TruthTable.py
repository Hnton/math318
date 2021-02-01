def getSym(x):
    if x:
        return '| True '
    else:
        return '| False'

values = [True, False]
print(" -------------------------------")
print("|   P  ", "|   Q  ", "| P=>Q ", "| P<=>Q |")
print(" -------------------------------")
for p in values:
    for q in values:
        print(getSym(p), getSym(q), getSym(not p or q), getSym((not p or q) and (not q or p)), "|")
        print(" -------------------------------")


