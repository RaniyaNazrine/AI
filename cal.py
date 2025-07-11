x=float(input("Enter number 1 : "))
y=float(input("Enter number 2 : "))

while True:
	n=input("Enter the operation \n1) addition\n2)subtraction\n3)multiplication\n4)division\n5)EXIT\n")
	if n == "1":
		print(x+y)
	elif n == "2":
		print(x-y)
	elif n == "3":
		print(x*y)
	elif n == "4":
		print(x/y)
	elif n == "5":
		print("Exit")
		break
	else:
		print("invalid entry")	
		
