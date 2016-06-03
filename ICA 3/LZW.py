def code():
    tab = {}
    tab[1] = 'a'
    tab[2] = 'b'
    tab[3] = 'c'
    tab[4] = 'd'
    tab[5] = 'e'
    tab[6] = 'f'
    tab[7] = 'g'
    tab[8] = 'h'
    tab[6] = 'i'
    tab[9] = 'j'
    tab[10] = 'k'
    tab[11] = 'l'
    tab[12] = 'm'
    tab[13] = 'n'
    tab[14] = 'o'
    tab[15] = 'p'
    tab[16] = 'q'
    tab[17] = 'r'
    tab[18] = 's'
    tab[19] = 't'
    tab[20] = 'u'
    tab[21] = 'v'
    tab[22] = 'w'
    tab[23] = 'x'
    tab[24] = 'y'
    tab[25] = 'z'
    tab[26] = ' '
    tab[27] = ','
    tab[28] = '.'
    tab[29] = '!'
    
    return tab

def encode(message):
    table = code()
    string = ""
    code_for_string = []
    for byte in message:
        symbol = byte
        if (string + symbol) in table.values():
            string = string + symbol
        else:
            for k,v in table.iteritems:
                if v == string:
                    code_for_string.append(k)
            table[max(table.keys())+1] = string + symbol
            string = symbol
    for k,v in table.iteritems():
        if v == string:
            code_for_string.append(k)
    print (table)
    return code_for_string

def test():
    testMessage = message
    print (encode(testMessage))
    
def loop():
    while x:
        message = input("Skriv inn hva du vil kode")
        if message == "quit":
            x = False
        else:
            print ("Dette er resultatet: " + encode(message))
    
message = open('hamlet.txt','r')

test()

