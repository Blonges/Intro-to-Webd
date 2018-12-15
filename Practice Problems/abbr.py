#provided input.txt for inputs.
#run as - python3 abbr.py < input.txt


contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

#print(contents)
answers=[]
for s in contents:
	x = s.split(" ")
	word=""
	for i in x:
		word = word + i[0]
	answers.append(word)

for item in answers:
	print(item)