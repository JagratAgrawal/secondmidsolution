n=input("enter a string")
rev=""
for i in n:
	rev=i+rev
print(rev)
if n==rev:
	print("this is palindrome")
else:
	print("this is not palindrome")
