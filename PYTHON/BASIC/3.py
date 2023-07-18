#Binary Datatypes- Bytes, Bytearray

MainList=[1,2,3,4,5];

#Bytes
BytesList=bytes(MainList);
print('MainList : ',MainList)
print('BytesList : ',BytesList) #Address
print('BytesList[0] : ',BytesList[0])
print('BytesList[1] : ',BytesList[1])
print('BytesList[2] : ',BytesList[2])
print('BytesList[3] : ',BytesList[3])
print('BytesList[4] : ',BytesList[4])

print('MainList[0] : ',MainList[0])
print('BytesList[0] : ',BytesList[0])
MainList[0]=5; #Updating main list do not update the bytes	
print('MainList[0] : ',MainList[0])
print('BytesList[0] : ',BytesList[0])

#BytesList[0]=5 : Error Cannot Update bytes (immutable)

'''-------------------------------------------------------------------------------'''

#Bytearray

MainList=[1,2,3,4,5]

ByteArrayList=bytearray(MainList)
print('MainList	: ',MainList)
print('ByteArrayList : ',ByteArrayList) #Address

for i in range(0,len(MainList)):
	print('ByteArrayList[',i,'] : ',ByteArrayList[i]);
print('ByteArrayList[0] : ',ByteArrayList[0])
ByteArrayList[0]=5 #Mutable
print('ByteArrayList[0] : ',ByteArrayList[0])



