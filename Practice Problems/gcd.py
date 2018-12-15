def gcd_recurr(x,y):
	r=x%y
	if r==0:
		return y
	else:
		return gcd_recurr(y,r)



print("Enter 2 numbers separated by space : ",end="")
x,y = map(int,input().split(" "))

#recurrsive implementation:
if x > y :
	print("GCD of",x,"&",y,"is",int(gcd_recurr(x,y)))
else:
	print("GCD of",x,"&",y,"is",int(gcd_recurr(y,x)))

#iterative implementaton:
r=x%y
while r!=0:
	x=y
	y=r
	r=x%y

print("GCD :",y)
