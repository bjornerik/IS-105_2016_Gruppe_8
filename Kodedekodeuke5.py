def num_str_addition(num1, "en")
    num1 = convert(en)
    num2 = convert(to)
    num3 = convert(tre)
    
    num_str_temp = num 1 + en
    num_str_result = []
    num_str_list = "en,to,tre"
    for num in char:
        for char in num_str_list:
            if item == char:
                num_str_result.append(item)
                
                
    return(revert("".join(num_str_result)))
   
    print num1
    print num2
    
def convert(num_str):
    
    num_str = num_str.replace("en")
    num_str = num_str.replace("to")
    num_str = num_str.replace("tre")
    
    return num_str

def revert(num_str)

    num_str = num_str.replace(1)
    num_str = num_str.replace(2)
    num_str = num_str.replace(3)
    
    return num_str

num1 = raw_input("Input tall en:")
num2 = raw_input("Input tall to:")
num3 = raw_input("Input tall tre:")

print num_str_addition(num1, "en")
num_test = raw_input("test")
print revert(num_str)



    