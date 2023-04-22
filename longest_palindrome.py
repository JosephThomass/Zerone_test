def largest_palindrome(string):
    # Initialize the largest palindrome to be an empty string
    largest_palindrome = ""
    
    # Loop through all substrings of the input string
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            substring = string[i:j]
            
            # Check if the substring is a palindrome
            if substring == substring[::-1]:
                # If the substring is longer than the current largest palindrome, update the largest palindrome
                if len(substring) > len(largest_palindrome):
                    largest_palindrome = substring
    # if the length of the series is less than or equal to 1 return none               
    if len(largest_palindrome)<2:
        largest_palindrome=None
    
    return largest_palindrome

string=input("Enter string: ")
print(largest_palindrome(string))
    
