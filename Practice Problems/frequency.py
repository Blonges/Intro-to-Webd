a = input().split(" ")
freq = {}
for x in a:
	if x not in freq:
		freq[x]=1
	else:
		freq[x]+=1

for x in freq:
	print(x,":",freq[x])