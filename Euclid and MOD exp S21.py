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
		print("d0=",d0,"d1=",d1,"q=",q,"x0=",x0,"x1=",x1,"x2=",x2,"y0=",y0,"y1",y1,"y2=",y2)
	return (d0,x0,y0)

def modexp(base, exponent, mod):
	prod=1
	while exponent>0:
		if exponent%2==1:
			prod=(prod*base)%mod
		base=base**2%mod
		exponent=exponent//2
	return prod

