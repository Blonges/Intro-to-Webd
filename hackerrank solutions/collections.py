n = int(input())
d={}
for i in range(n):
    line = input().split(" ")
    l = len(line)
    name = line[0]
    for k in range(1,l-1):
    	name = name +" " + line[k]

    if name not in d:
        d[name] = int(line[l-1])
    else:
        d[name] += int(line[l-1])

for x in d:
    print(x,d[x])