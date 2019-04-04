n=input("enter a string\n")
a=""
b=""
for i in n:
	d=ord(i)
	if d>=65 and d<=90:
		a=a+i
	else:
		b=b+i
print("Capital letters",a)
print("Other characters",b)
