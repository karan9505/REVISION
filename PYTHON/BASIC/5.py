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

#--------------------------------------------------------------------------------#

#Tuple
Tuple=(1,2,3,4,5);

print(Tuple.__sizeof__())
print('Tuple : ',List)
for i in range(0,len(Tuple)): #Accessing using index
	print('Tuple',i,':',Tuple[i])

for i in range(-len(Tuple),0,1): #Accessing using negitive index
	print('Tuple',i,':',Tuple[i])

#Tuple[0]=100; Imutable

#---------------------------------------------------------------------------------#
String="Mystring"

print(String	)
print(String.__sizeof__	())
print(type(String))