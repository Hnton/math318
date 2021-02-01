print("First:")
f = input()
print("Second:")
s = input()



def iff(f, s):
    print("----IFF----")
    if f == s:
        
        print("True")
    else:
        print("False")

iff(f,s)

def implies(f,s):
    print("----IMPLIES----")
    if f == "True":
        
        print("False")
    else:
        print("True")

implies(f,s)
