my_file = open("File.txt",'r')
file_contents = my_file.read()
counts = {}
for word in file_contents.split():
    if word not in counts:
       counts[word] = 0
       counts[word] += 1
print(counts)

'''my_file = open("File.txt",'r')
my_string= my_file.read()
my_dict={}
for item in my_string:
  my_dict[item] = my_string.count(item)
print(my_dict)'''

'''def search(File, wordtofind):
         f=open(File.txt, 'r')
         text=f.read()
         f.close()
         count = 0
         index = text.find(wordtofind)
         while(index !=-1):
             count += 1
             text = text[index+len(wordtofind):]
             index = text.find(wordtofind)
         return count

search(File.txt, to)'''


"""wordcheck = input("Please enter the word you want to find in the file : ")
with open("File.txt", 'r') as f :
    found = False 
    for line in f:
        if line.split()==wordcheck:
            print('That is found' +wordcheck)
            found= True
            break
    if not found :
        print(wordcheck+ " is not in the file")"""