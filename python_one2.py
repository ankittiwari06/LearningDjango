my_file = open("File.txt",'r')
file_contents = my_file.read()
values=file_contents.split()
filelist=[]
for w in values:
	filelist.append(values.count(w))
print(zip(values, filelist))
