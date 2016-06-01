<<<<<<< HEAD:ICA 01/ICA 01.py
def Encode():
    string = []
    prompt = input("Skriv inn hva du vil kode ned: ")
    prompt.split()
    for x in prompt:
        if x == "X":
            string.append("01")
        elif x == "Y":
            string.append("10")
        elif x == "Z":
            string.append("11")
    print (string)
=======
def tolk():
    while 1:
        encoding = raw_input('Encode >')
        liste = encoding.split()
        string = []
        for x in liste:
            if x == "X":
                string.append("01")
            elif x == "Y":
                string.append("10")
            elif x == "Z":
                string.append("11")
        print string
>>>>>>> origin/master:ICA 02.py
    
Encode()
    
