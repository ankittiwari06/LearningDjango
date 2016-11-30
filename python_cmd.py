from cmd import Cmd
import re
import random

class Mycmd(Cmd):


    #def fileread(file):
     #   file = input ("Enter the fileName : ")
      #  my_file = open(file, 'r')
       # file_contents = my_file.read()
        #return file_contents

    
    def do_openfile(self, args):
        file = input("Enter file name : ")
        my_file = open(file,'r')
        file_contents = my_file.read()
        values=fileread()
        print(values)    

    def help_openfile(self):
        print("Open an specific File.")

    def do_wordcount(self, args):
        file = input("Enter file name : ")
        my_file = open(file,'r')
        file_contents = my_file.read()
        values = file_contents.split()
        counts = []
        for word in values:
            counts.append(values.count(word))
        print(list(zip(values, counts)))

    def help_wordcount(self):
        print("Count the no of times all the word repeated in files.")

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
    
    def help_search(self):
        print("How many times the word is repeated in fies.")

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
        

    def help_show(self):
        print("This function is under working")

    def do_randomword(self, args):
        file = input("Enter file name : ")
        my_file = open(file,'r')
        file_contents = my_file.read()
        values = file_contents.split()
        print(random.sample(values,10))


    def help_randomword(self):
        print("Show 10 random word from the File.")

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

    def help_wordlength(self):
        print("Print all the word whose length is greater than the user input word.")
        
    
    def do_starpattern1(self, args):
        for i in range(0, 5):
            for j in range(i , 5):
                print(" * ", end=" ")
            print()
            


    def help_starpattern1(self):
        print("Print the below star pattern")
        print("* * * * * ")
        print("* * * * ")
        print("* * * ")
        print("* * ")
        print("* ")

    def do_starpattern2(self, args):
        k = 8
        for i in range(0, 5):
            for j in range(0, k):
                print(end=" ")
            k = k - 2
            for j in range(0, i+1):
                print("* ", end="")
            print()


    def help_starpattern2(self):
        print("Print the below star pattern")
        print("* ")
        print("* * ")
        print("* * * ")
        print("* * * * ")
        print("* * * * * ")


    def do_starpattern3(self,args):
        k = 0
        rows = 10
        for i in range(1, rows+1):
            for space in range(1, (rows-i)+1):
                print(end="  ")
            while k != (2*i-1):
                print("* ", end="")
                k = k + 1
            k = 0
            print()


    def help_starpattern3(self):
        print("Print the below star pattern")
        print("          *          ")
        print("        * * *        ")
        print("      * * * * *      ")
        print("    * * * * * * *    ")
        print("  * * * * * * * * *  ")
        print("* * * * * * * * * * *")




    def do_degree2radian(self, args):
        degree = float(input("Enter the value in Degree : "))
        pi = 22/7
        radian = degree*(pi/180)
        print("The Value in Radian is ", radian)


    def help_degree2radian(self):
        print("Convert degree to radian.")

    def do_is_allowed_specific_char(self, string):
        charRe = re.compile(r'[^a-zA-Z0-9.]')
        string = charRe.search(string)
        return not bool(string)

        print(do_is_allowed_specific_char(input("Enter the String : "))) 


    def help_is_allowed_specific_char(self):
        print("Check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9). If yes the print True else print False")

    def do_add2no(self,s):
        l = s.split()
        if len(l)!=2:
            print("Invalid number of arguments")
            return
        try:
            l = [int(i) for i in l]
        except ValueError:
            print("arguments should be numbers")
            return
        print(l[0]+l[1])

    def help_add2no(self):
        print("This function takes two arguemented seperated by space and print the add of both arguements.")

    def do_quit(self, args):
        print("Quitting.")
        raise SystemExit

    def help_quit(self):
        print("This function close the command prompt")

#By default when an empty line is entered, the last command is repeated. so by overriding the emptyline method we can change this behaviour of Command Prompt.
#For example to disable the repetition of the last command: 
    def emptyline(self):
        pass


if __name__ == '__main__':
    values = Mycmd()
    values.prompt = '>>'
    values.cmdloop('Starting cmd Prompt...')
