# Mikael Hinton
# Project 10

def eucx(d0,d1):
	x0=1
	y0=0
	x1=0
	y1=1
	while d1 !=0:
		q=d0//d1
		d2=d1
		x2=x1
		y2=y1
		d1=d0%d1
		x1=x0-q*x1
		y1=y0-q*y1
		d0=d2
		x0=x2
		y0=y2
		# print("d0=",d0,"d1=",d1,"q=",q,"x0=",x0,"x1=",x1,"x2=",x2,"y0=",y0,"y1",y1,"y2=",y2)
	return (d0,x0,y0)

def modexp(base, exponent, mod):
	prod=1
	while exponent>0:
		if exponent%2==1:
			prod=(prod*base)%mod
		base=base**2%mod
		exponent=exponent//2
	return prod

p=10174093
q=10176827
print()
print("p:",p)
print("q:",q)
#Find the M
m = p*q
print("m:",m)
#Find the phi
phi = (p-1)*(q-1)
print("phi:",phi)

#Pick an E
e = 1009
print("e:",e)

#Find decryption Exponent
s = eucx(e, phi)
print()
print("Euclidian Algorithm Extended:",s)
#middle number of eucx, make sure to get a 1 and if you dont then change e
d = 5130820812289

amsg = "Math"
msg = [ord(c) for c in amsg]

def convert(msg):
    s = [str(i) for i in msg]
    res = int("0".join(s))

    return(res)

cmsg = int(convert(msg))
print("                     Message:", amsg)

print("            Message in ASCII:", cmsg)
#encode msg
cipher = modexp(cmsg, e, m)
print("                   Encrypted:", cipher)
#decrypt msg
decr = modexp(cipher, d, m)
print("                   Decrypted:", decr)
print()
