from cmd import Cmd
import re

class Mycmd(Cmd):

    
    def do_fileopen(self, args):
        my_file = open("File.txt",'r')
        file_contents = my_file.read()
        print(file_contents)

    def do_wordcount(self, args):
        my_file = open("File.txt",'r')
        file_contents = my_file.read()
        values = file_contents.split()
        counts = []
        for word in values:
            counts.append(values.count(word))
            print(list(zip(values, counts)))

    def do_search(self, args):
        total = 0
        ip = input("Please enter the word you want to find in the file : ")
        with open('File.txt') as f :
            for line in f:
                finded=line.find(ip)
                if finded != -1 and finded != 0 :
                    total += 1
        print(total)
    
    def do_show(self, args):
        my_file = open("File.txt",'r')
        file_contents = my_file.read()
        values = file_contents.split()
        counts = []
        for word in values:
            counts.append(values.count(word))
            filelist = list(zip(values, counts))
        for element in filelist :
            p = re.compile(r'^t')
            m = p.search("this is the and the tiger is a byth")
        print(m)

    def do_quit(self, args):
        print("Quitting.")
        raise SystemExit

if __name__ == '__main__':
    values = Mycmd()
    values.prompt = 'ankit '
    values.cmdloop('Starting cmd...')