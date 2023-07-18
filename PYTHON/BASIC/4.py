#Command Line Argument

import sys
#sys.argv is list of all command line arguments

print(type(sys.argv))
print(sys.argv)

for i in range(0,len(sys.argv)):
	if(i==0):
		print('File name : ',sys.argv[i]) #First element of list is file name
	else:
		print('Element',i,' : ',sys.argv[i])