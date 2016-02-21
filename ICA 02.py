def tolk():
    liste = ['X','Y','Z', 'Y', 'Z']
    string = []
    for x in liste:
        if x == "X":
            string.append("01")
        elif x == "Y":
            string.append("10")
        elif x == "Z":
            string.append("11")
    print string
    
tolk()
    
