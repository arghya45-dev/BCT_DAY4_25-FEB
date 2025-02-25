import functions

num = int(input ("enter a number "))

# Call Fibonacci function
print(f"Fibonacci series to {num} is: {functions.fibonacci(num)}")


# Call Prime check function
if functions.prime(num) :
    print(f"{num} its a prime number")
else:
    print(f"{num} its not a prime number ")


# Call Factorial function
if functions.factorial(num) :

 print(f"Factorial of {num} is: {functions.factorial(num)}")