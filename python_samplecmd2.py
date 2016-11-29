from cmd import Cmd
import re
import random

class Mycmd(Cmd):

    
    def do_openfile(self, args):
        file = input("Enter file name : ")
        fhand = open(file,'r')
        full_txt = fhand.read()
        print(full_txt)    

    def do_wordcount(self, args):
        my_file = open("/home/ankit/Python_practise/file1.txt",'r')
        file_contents = my_file.read()
        values = file_contents.split()
        counts = []
        for word in values:
            counts.append(values.count(word))
        print(list(zip(values, counts)))

    def do_search(self, args):
        total = 0
        ip = input("Please enter the word you want to find in the file : ")
        with open('/home/ankit/Python_practise/File.txt') as f :
            for line in f:
                finded=line.find(ip)
                if finded != -1 and finded != 0 :
                    total += 1
        print(total)
    
    def do_show(self, args):
        my_file = open("/home/ankit/Python_practise/File.txt",'r')
        file_contents = my_file.read()
        values = file_contents.split()
        counts = []
        for word in values:
            counts.append(values.count(word))
            filelist = list(zip(values, counts))
        for element in filelist :
            p = re.compile(r'^t')
            m = p.search("this is the and the tiger is a byth")
        

    def do_randomWord(self, args):
        my_file = open("/home/ankit/Python_practise/file1.txt",'r')
        file_contents = my_file.read()
        values = file_contents.split()
        print(random.sample(values,10))


    def do_lengthword(self, args):
        word=input("Word is : ")
        w1=len(word)
        my_file = open("/home/ankit/Python_practise/file1.txt",'r')
        file_contents = my_file.read()
        values = file_contents.split()
        for w in values:
            if len(w)>w1:
                print(w)
            


    def do_quit(self, args):
        print("Quitting.")
        raise SystemExit

if __name__ == '__main__':
    values = Mycmd()
    values.prompt = '>>'
    values.cmdloop('Starting cmd Prompt...')
