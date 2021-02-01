import itertools

print("Enter the number")
n = input()
n = int(n)
print(n)
r=2**n
line="+---"*n+"+"
for i in range(r):
    a = "|"
    print(line)
    for j in range(n):
        if(i//(r/2**(j+1)))%2==0:
            a= a+" T |"
            continue
        a=a+" F |"
    print(a)

table = list(itertools.product([True, False], repeat = n))
data =list(zip(table))

for  i in enumerate(data):
    line = ''.join(str(x).ljust(0) for x in i)
    print(line)
    if i == 0:
        print('-' * len(line))

