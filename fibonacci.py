def fibonacci(number):
    # initilize first 2 number of fibonacci series
    num1=0
    num2=1
    # Calculate fibonacci above range 2
    for i in range (2,number):
        sum=num1+num2
        num1 =num2
        num2= sum
    return sum
    
# Take input 
number=int(input(">"))
# Return number if the number is lower than 2 if above call the function
if number<=1:
    print(number)
else:
    result = fibonacci(number)
    print(result)


