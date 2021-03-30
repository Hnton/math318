# Mikael Hinton
# Project 9
# Functions from https://stackoverflow.com/questions/37237954/calculate-the-lcm-of-a-list-of-given-numbers-in-python

a = [9720,4158,594,612]

def euc(a,b):
	c=list(range (2))
	if a>b:
		c[0], c[1]=a, b
	if b>a:
		c[0], c[1]=b, a
	while c[1]>0:
		d=c[0]%c[1]
		c[0]=c[1]
		c[1]=d
		gcd=c[0]
		if c[1]==1:
			gcd=1
			break
	return gcd

#Compute first 2 numbers
f = euc(a[0],a[1])
#Compute result from first 2 and 3rd number
s = euc(f,a[2])
#Compute result from 2nd and 3rd number with 4th number
l = euc(s,a[3])

lcm = a[0]
for i in a[1:]:
  lcm = lcm*i//euc(lcm, i)

print("Least Common Multiple: ",lcm)

print("Greatest Common Factor: ", l)
