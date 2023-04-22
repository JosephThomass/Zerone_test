def isvalid(my_string):
    # Stack for left symbols
    left_symbols = []
    # Loop for each character of the string
    for symbol in my_string:
        # If left symbol is encountered
        if symbol in ['(', '{', '[']:
            left_symbols.append(symbol)
        # If right symbol is encountered
        elif symbol == ')' and len(left_symbols) != 0 and left_symbols[-1] == '(':
            left_symbols.pop()
        elif symbol == '}' and len(left_symbols) != 0 and left_symbols[-1] == '{':
            left_symbols.pop()
        elif symbol == ']' and len(left_symbols) != 0 and left_symbols[-1] == '[':
            left_symbols.pop()
        # If none of the valid symbols is encountered
        else:
            return False
    return left_symbols == []
mystring=input("Enter sting: ")
result=isvalid(mystring)
print(result)