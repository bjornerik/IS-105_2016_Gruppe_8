import os.path
import mmap

class Folder(object):
    pass

class File(object):
    pass

# write a simple example file
with open("hello.txt", "wb") as f:
    f.write(b"Hello Python!\n")

with open("hello.txt", "r+b") as f:
    # memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # read content via standard file methods
    print(mm.readline())  # prints b"Hello Python!\n"
    # read content via slice notation
    print(mm[:5])  # prints b"Hello"
    # update content using slice notation;
    # note that new content must have same size
    mm[6:] = b" world!\n"
    # ... and read again using standard file methods
    mm.seek(0)
    print(mm.readline())  # prints b"Hello  world!\n"
    # close the map
    mm.close()

def isFile(fil):
    if os.path.isfile(fil):
        print (fil + " finnes")
    else:
        print(fil + "Finnes ikke")

    
def displayCommands(path):
    if path == "3":
        print("The following commands is possible")
        print("isfile")
    
def fileloop():
    path = ["C", "M", "fil"]
    print (path)
    
    while True:
        print ("You are here: ")
        for element in path:
            print (element + "/")
        print ("Type cmd to display possible commands")
        command = input(">")
        if len(path) == 2:
            if command == "cmd":
                displayCommands("3")
            if command == "isfile":
                file = input("Which file do you want to check if exists?")
                isFile(file)


            
fileloop()
            
        