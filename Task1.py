def reverse_integer(number):
    # check if input is negative
    is_negative = False
    if number < 0:
        is_negative = True
        number = -number
        
    # reverse the number
    rev_num = 0
    while number > 0:
        rev_num = rev_num * 10 + number % 10
        number //= 10
    
    # check if within range of signed 32-bit integer
    if rev_num > 2**31-1:
        print(0)
    elif is_negative and rev_num >= 2**31:
        print(0)
    elif is_negative:
        print(-rev_num)
    else:
        print(rev_num) 

num=int(input("Enter the number: "))
reverse_integer(num)
