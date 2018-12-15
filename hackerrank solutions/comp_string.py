from itertools import groupby

n = input()
answers = []
for k,g in groupby(n):
	p = (len(list(g)),int(k))
	answers.append(p)

for x in answers:
	print(x,end=" ")
print("")