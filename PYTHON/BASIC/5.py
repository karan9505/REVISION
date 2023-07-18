#Sequence Datatypes- List, Tuple, String, Range

List=[1,2,3,4,5,6];

print('List : ',List)
for i in range(0,len(List)): #Accessing using index
	print('List',i,':',List[i])

for i in range(-len(List),0,1): #Accessing using negitive index
	print('List',i,':',List[i])

List[0]=100; #Mutable


Tuple=(1,2,3,4,5,6);

print('List : ',List)
for i in range(0,len(List)): #Accessing using index
	print('List',i,':',List[i])

for i in range(-len(List),0,1): #Accessing using negitive index
	print('List',i,':',List[i])

List[0]=100; #Mutable