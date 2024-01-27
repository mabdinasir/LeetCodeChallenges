def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	for k in d.keys():	
		print(k)

# printDict()

def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	for (k,v) in d.items():	
		print(v)

# printDict()
		
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print(li)

# printList()

def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print(li[-5:])

# printList()

#Change list to a tuple
def printTuple():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print(tuple(li))
		
# printTuple()

#Print each half of a tuple in a list
tp=(1,2,3,4,5,6,7,8,9,10)
tp1=tp[:5]
tp2=tp[5:]
# print(tp1)
# print(tp2)

#print even numbers only from a tuple
tp=(1,2,3,4,5,6,7,8,9,10)
li=list()
for i in tp:
	if i%2==0:
		li.append(i)

tp2=tuple(li)
# print(tp2)

#print yes if string is "YES" or "yes" or "Yes"
def printYes():
	s=input("Enter a string: ")
	if s=="YES" or s=="yes" or s=="Yes":
		print("Yes")
	else:
		print("No")

# printYes()

#
