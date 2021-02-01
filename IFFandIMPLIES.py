# print("First:")
# f = input()
# print("Second:")
# s = input()



def iff(f, s):
    print("----IFF----")
    if f == s:
        
        print("True")
    else:
        print("False")

# iff(f,s)

def implies(f,s):
    print("----IMPLIES----")
    if f == "True":
        
        print("False")
    else:
        print("True")

# implies(f,s)

def getSym(x): 
    if x: 
        return 'T' 
    else: 
        return 'F' 

values=[True, False] 
for p in values: 
    for q in values:
        print(getSym(p), getSym(q), getSym(p and q))    #  AND
        print(getSym(p), getSym(q), getSym(p or q))     #  OR
        print(getSym(p), getSym(q), getSym(not p or q)) #  =>
        print(getSym(p), getSym(q), getSym(p == q))     #  <=>
