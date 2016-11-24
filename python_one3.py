#import msvcrt

#print("press 'escape' to quit...")

#while 1:
#    char = msvcrt.getch()
#    if char == chr(27):
#        break
#    print(char),
#    if char == chr(13):
#        print("done")
import msvcrt
while True:
if(msvcrt.kbhit()):
key = msvcrt.getch()
if key == 'Enter'
  my_file = open("File.txt",'r')
  file_contents = my_file.read()
  counts = {}
  for word in file_contents.split():
    if word not in counts:
       counts[word] = 0
       counts[word] += 1
  print(counts)
