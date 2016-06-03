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
    
Encode()
    
