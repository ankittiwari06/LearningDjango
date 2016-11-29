#from collections import Counter
#my_file = open("/home/ankit/Python_practise/file1.txt",'r')
#file_contents = my_file.read()
#print(file_contents)
#values = list(map(str, file_contents.split()))
#print(Counter(values))
def function_filename(file):
    my_file = open(file, 'r')
    return my_file
file=input("File : ")
print(function_filename(file))