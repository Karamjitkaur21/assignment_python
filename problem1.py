def is_valid_number(num, base):
    array = [int(part) for part in num.split("-")]
    for digit in array:
        if int(digit) >= base:
            return False
    return True

def base_conv(num, base, new_base):
    if not is_valid_number(num, base):
        print("Invalid number for the given base.")
        return
    
    num = [int(part) for part in num.split("-")]
    num_base10 = 0
    num_len = len(num)
    for i, digit in enumerate(num[::-1]):
          num_base10 += int(digit) * (base ** i)
    
    
    result = ""
    while num_base10 > 0:
        remainder = num_base10 % new_base
        result = str(remainder) + "-" + result
        num_base10 //= new_base
    
    result = result.rstrip("-")
    print(result)

base_conv("1-2-3-45-6", 44, 23)
base_conv("1-2-3-45-6", 46, 23)
base_conv("6-54-3-21", 46, 23)
base_conv("6-54-3-21", 63, 74)