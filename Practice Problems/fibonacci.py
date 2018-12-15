def fibo(n,a1,a2):
	if n>2:
		a3 = a1+a2
		print(a3)
		fibo(n-1,a2,a3)

n = int(input("Enter n : "))

if n==1:
	print("0")
elif n==2:
	print("0")
	print("1")
else :
	print("0")
	print("1")
	fibo(n,0,1)