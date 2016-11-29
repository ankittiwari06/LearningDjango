#Write a program which can compute the factorial of a given numbers.
def fact(x):
	if(x==0):
		return 1
	return x*fact(x-1)
x=int(input("Find the Factorial of : "))
print(fact(x))