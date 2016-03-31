import os.path
import sys
import mmap

os.chdir("C:\\Users\Sjur\Documents\Filsystem")   

def isdir(dirname):
    return os.path.exists(dirname)

def isfile(fil):
    return os.path.isfile(fil + ".txt")

class Folder(object):
    def __init__(self, name):
        self.name = name
        if not os.path.exists(self.name):
            os.mkdir(self.name) 
        
class File(object):
    def __init__(self, navn):
        self.navn = navn
        file = open((navn + ".txt"), "w")
        file.write(" ")
        file.close()  
        
def write(name, text):
    with open(name + ".txt", "w") as f:
        f.write(text)
        f.close()
        
def read(name):
    with open(name + ".txt") as f:
        print(f.read())
        f.close()
        
def searchWord(name, word):
    with open(name + ".txt") as f:
        for line in f:
            if word in line:
                print(word + " is found at position " + str(len(line)) + " in " + name)
    

    
def displayCommands(path):
    print("The following commands is possible")
    if path == "1":
        print("isdir")
        print("opendir")
        print("createdir")
        print("quit")
    if path == "2":
        print("isfile")
        print("cd..")
        print("createfile")
        print("write")
        print("read")
        print("searchWord")
        print("quit")
    
def fileloop():
    x = True
    count = 1
    
    
    while x:
        path = os.getcwd()
        print ("You are here: ")
        #print (" \ ".join(path))
        print (path)
        print ("Type cmd to display possible commands")
        command = input(">")
        if command == "quit":
            x = False
        if count == 1:
            if command == "cmd":
                displayCommands("1")
            if command == "isdir":
                thedirectory = input("Which folder do you want to check if exist?\n")
                if isdir(thedirectory):
                    print(thedirectory + " finnes")
                else:
                    print(thedirectory + " finnes ikke")                    
            if command == "opendir":
                thedirectory = input("Which folder do you want to open?\n")
                if isdir(thedirectory):
                    count = 2
                    os.chdir(thedirectory)
                else: 
                    print ("The folder you tried to open doesn't exist")

            if command == "createdir":
                navn = input("What do you want to name the folder?\n")
                Folder(navn)
        
        if count == 2:
            if command == "cmd":
                displayCommands("2")            
            if command == "isfile":
                thefile = input("Which file do you want to check if exist?\n")
                if isfile(thefile):
                    print(thefile + " finnes")
                else:
                    print(thefile + " finnes ikke")
                    
            if command == "cd..":
                count = 1
                os.chdir("C:\\Users\Sjur\Documents\Filsystem")
                    
            if command == "createfile":
                filnavn = input("What do you want to name the file?\n")
                File(filnavn)
            
            if command == "write":
                thefile = input("Which file do you want to write in?\n")
                if isfile(thefile):
                    text = input("What do you want to write?\n")
                    write(thefile, text)
                    print (text + "\nwas written in " + thefile)
                else:
                    print ("The file you tried to open doesn't exist")
            
            if command == "read":
                thefile = input("Which file do you want to read?\n")
                if isfile(thefile):
                    read(thefile)
                else:
                    print ("The file you tried to open doesn't exist")        
            
            if command == "searchWord":
                thefile = input("Which file do you want to search in?\n")
                if isfile(thefile):
                    word = input("What word do you want to search for?\n")
                    searchWord(thefile, word)
                else:
                    print ("The file you tried to open doesn't exist") 
                
fileloop()
                
        
        
        


            

            
        