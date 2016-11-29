#Define a class which has at least two methods:
#getString: to get a string from console input
#printString: to print the string in upper case.
class Test(object):
	def __init__(self):
		self.n = ""
	def getString(self):
		self.n = input("Enter the String : ")
	def printString(self):
		print("String in UpperCase is : ",self.n.upper())
obj = Test()
obj.getString()
obj.printString()