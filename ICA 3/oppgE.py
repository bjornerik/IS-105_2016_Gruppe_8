def encode(order):
    danger = [0, 9, 10, 13, 32, 222, 255, 256]
    str2 = ""
    str3 = ""
    binary = bin(order)[2:]
    for bit in binary:
        str2 += bit
        if len(str2) == 8:
            helper = int(str2,2)
            if helper in danger:
                str3 = chr(222)+str(order)
                str2 = ""
                break
            else:
                str3 += chr(int(str2,2)) 
                str2 = ""
    if str2 != "":
        helper = int(str2,2)
        if helper in danger:
            str3 = chr(222)+str(order)
        else:
            str3 += chr(int(str2,2))
    return str3

file_in = open("hamlet.txt")
file_out = open("compressed5.txt","w")

codes = dict([(chr(x), x) for x in range(256)])
danger = [0, 9, 10, 13, 32, 222, 255, 256]      
code_count = 257
current_string = ""
string = file_in.read()
for c in string:
    current_string = current_string + c
    if not current_string in codes:
        codes[current_string] = code_count
        if (codes[current_string[:-1]] < 257) & (codes[current_string[:-1]] not in danger):
            file_out.write(chr(codes[current_string[:-1]])+" ")
        else:
            str4 = encode(codes[current_string[:-1]])
            file_out.write(str4+" ")
        code_count += 1
        current_string = c
file_out.write(encode(codes[current_string]))

file_in.close()
file_out.close()