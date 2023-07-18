#Numeric Datatypes- Int,Float,Complex

#Int
a=100
print('Data type : ',type(a),'|| Size : ',a.__sizeof__())

#Float
b=10.10
print('Dta type : ',type(b),' || Size : ',b.__sizeof__())

#Complex
c=complex(1,2);
d=complex(3,4);
print('Data type : ',type(c),' || Size : ',c.__sizeof__	())

print(c+d)
print(c-d)
print(c/d)
print(c*d)