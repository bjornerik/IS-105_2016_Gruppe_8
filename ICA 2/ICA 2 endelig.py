letterToBinary = {'A':'0', 'B':'1', 'C':'00', 'D':'01', 'E':'11', 'F':'000'}
binaryToLetter = dict((v, k) for k, v in letterToBinary.iteritems())

def encode(string):
    inpuT = string
    output = '' 
    total = ''
    
    for i in inpuT:
        total += i 
        if letterToBinary.has_key(total):
            output += letterToBinary[total]
            total = ''
        return output

def decode(string):
    inpuT = string
    output = '' 
    total = ''
    
    for i in inpuT:
        total += i 
        if binaryToLetter.has_key(total):
            output += binaryToLetter[total]
            total = '' 
    return output

def loop():
    while True:
        kommando = input("Do you want to decode or encode? \n")
        if kommando == 'encode':
            string = input("What do you want to encode? \n")
            print (encode(string))
        if kommando == 'decode':
            string = input("What do you want to decode? \n")   
            print (decode(string))
            
            
loop()