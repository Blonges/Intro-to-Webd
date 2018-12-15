#input from a file input_commas.txt
#$python3 commas.py < input_commas.txt
contents=[]
while True:
	try:
		line=input()
	except EOFError:
		break
	contents.append(line)

for n in contents:
	l = len(n)-3
	while l>0 :
		n=n[:l]+","+n[l:]
		l = l - 3
	print(n)