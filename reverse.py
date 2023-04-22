def reverse_integer(x):
    # check if input is negative
    is_negative = False
    if x < 0:
        is_negative = True
        x = -x
        
    # reverse the integer
    x_rev = 0
    while x > 0:
        x_rev = x_rev * 10 + x % 10
        x //= 10
    
    # check if within range of signed 32-bit integer
    if x_rev > 2**31-1:
        return 0
    elif is_negative and x_rev >= 2**31:
        return 0
    elif is_negative:
        return -x_rev
    else:
        return x_rev

    
num=int(input("Enter the number: "))
print(reverse_integer(num))
