#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 1000 and 3000 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

list = []
for i in range(1000,3001):
	if((i%7==0) and (i%5!=0)):
		list.append(str(i))
print(','.join(list))
