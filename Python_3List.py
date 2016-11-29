#Given three lists of numbers, write a small code using python where you find numbers that occur in all three lists

# your code goes here
def return_duplicates(list1, list2, list3):
	L1 = set(list1)
	L2 = set(list2)
	L3 = set(list3)
	l1 = L1.intersection(L2)
	l2 = l1.intersection(L3)
	return l2
	
list1 = [int(x) for x in input().split()]
list2 = [int(x) for x in input().split()]
list3 = [int(x) for x in input().split()]
print(return_duplicates(list1, list2, list3))
