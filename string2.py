n1=input("enter a string\n")
n2=input("enter a string\n")
if n1 in n2:
	print(n1,"is substring of",n2)
if n2 in n1:
	
	print(n2,"is substring of",n1)
else:
	print("no substring")
