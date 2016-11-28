from cmd import Cmd
import re
import random

class Mycmd(Cmd):

    
    def do_openfile(self, args):
        file = input("Enter file name : ")
        my_file = open(file,'r')
        file_contents = my_file.read()
        print(file_contents)    

    def do_wordcount(self, args):
        file = input("Enter file name : ")
        my_file = open(file,'r')
        file_contents = my_file.read()
        values = file_contents.split()
        counts = []
        for word in values:
            counts.append(values.count(word))
        print(list(zip(values, counts)))

    def do_search(self, args):
        total = 0
        file = input("Enter file name : ")
        ip = input("Please enter the word you want to find in the file : ")
        with open(file,'r') as f :
            for line in f:
                finded=line.find(ip)
                if finded != -1 and finded != 0 :
                    total += 1
        print(total)
    
    def do_show(self, args):
        file = input("Enter file name : ")
        my_file = open(file,'r')
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
        file = input("Enter file name : ")
        my_file = open(file,'r')
        file_contents = my_file.read()
        values = file_contents.split()
        print(random.sample(values,10))


    def do_wordlength(self, args):
        file = input("Enter file name : ")
        my_file = open(file,'r')
        file_contents = my_file.read()
        values = file_contents.split()
        word=input("Word is : ")
        w1=len(word)
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
