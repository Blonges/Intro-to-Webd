#print("My first program")

# print("Enter name")
# name = input()
# print("Hello, "+name)

# a=3**2
# print(a)
"""
print("Enter number")
n= int(input())
print("It's multiplication table is :")
for i in range(1,11):
	print(n,"x",i,"=",n*i)
"""

# runs = [ 1 , 2 , 3, 4 , 5 ]
# names = [ "Paul" , "Rashi" , "Bug" ]
# print(runs)
# print(names)

#prime numbers using sieve method

# arr = [1]*101

# for i in range(2,101):
# 	if arr[i]==1:
# 		for j in range(2*i,101,i):
# 			arr[j]=0

# for i in range(2,101):
# 	if arr[i]==1:
# 		print(i,"is a prime")

#nCr and nPr

# def factorial(n):
# 	ans = 1
# 	for i in range(1,n+1):
# 		ans=ans*i
# 	return ans

# def nCr(n,r):
# 	ans = factorial(n) / (factorial(r)*factorial(n-r))
# 	return ans

# def nPr(n,r):
# 	return nCr(n,r)*factorial(r)


# n=int(input("Enter n : "))
# r=int(input("Enter r : "))
# print("nCr =",int(nCr(n,r)))
# print("nPr =",int(nPr(n,r)))

# def cube(n):
# 	return n*n*n

# a = list(map(int,input().split(" ")))
# print(a)
# print(list(map(cube,a)))


# def datechange(n):
# 	a=n.split("-")
# 	a[0],a[1]=a[1],a[0]
# 	a="-".join(a)
# 	return a

# n = input("Enter date list mm-dd-yyyy: ").split()
# print(n)
# n = list(map(datechange,n))
# print(n)

# def hanoi(size, start, middle, end):
# 	if size > 0 :
# 		hanoi( size-1 , start , end , middle )
# 		print( "Move disk" , size , "from" , start , "to" , end )
# 		hanoi( size-1 , middle , start , end )

# n = int(input())
# hanoi(n,"A","B","C")

#check palindrome using list compehension
# a = [ 'a' , 'abc' , 'abcabc', 'abcba' ]
# b= [ item for item in a if item==item[::-1]]
# print(b)

# b= []
# for i in range(1,11):
# 	ans = 2**i
# 	b.append(ans)
# print(b)

# n = int(input("Enter the number of points : "))
# points = []
# print("Enter 3 decimals separated by space for each point")
# for i in range(n):
# 	print("Coordinates of point",i+1,":",end=" ")
# 	x,y,z = map(float,input().split())
# 	p = (x,y,z)
# 	points.append(p)
# print(points)

# r = int(input("Rows = "))

# a = []
# for i in range(r):
# 	a.append(list(map(int,input().split(" "))))
# b=[]
# for i in range(r):
# 	b.append(list(map(int,input().split(" "))))

# for i in range(r):
# 	print([ x+y for x,y in zip(a[i],b[i])])

# rolls1 = {1,3,5,6}
# rolls2 = {1,6,5,3}
# rolls3 = {2,4}
# if rolls2 == rolls1 :
# 	print("rolls2 is subset of rolls1")
# if rolls1.isdisjoint(rolls3) :
# 	print("disjoint sets")

