#fibonacci
def fibonacci (n):
    a,b = 0,1
    series=[]
    
    for i in range (n):
        series.append(a)
        a,b = b,a+b
        
    return series

# factorial
def factorial(n):
    if n==0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
        

# prime
def prime(n):
    if (n<2):
     return False
    for i in range(2, int(n ** 0.5) + 1):
     if n % i == 0:
       return False
    return True 