f1 = open("rolls/list1.txt","r")
f2 = open("rolls/list2.txt","r")
f3 = open("rolls/list3.txt","r")
fo = open("output.txt","w")

# l1 = f1.readlines()
# l2 = f2.readlines()
# l3 = f3.readlines()

# #print(l1)
# l = l1 + l2 + l3
# #print(l)
# l = [ int(x.strip()) for x in l]
# #print(l)
# l.sort()
# fo.write("Sorted :\n")
# l = [ str(x)+", " for x in l]
# fo.writelines(l)

l = f1.read()
print(l)

f1.close()
f2.close()
f3.close()
fo.close()
