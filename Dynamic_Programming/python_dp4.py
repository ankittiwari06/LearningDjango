#Write a program which accepts a sequence of comma-separated numbers from console and generate a list 
#and a tuple which contains every number. Suppose the following input is supplied to the program:
n = input("Enter the values : ")
x = n.split(" ")
t = tuple(x)
print(x)
print(t)