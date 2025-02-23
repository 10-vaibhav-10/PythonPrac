# #sum of nth term of natural numbers
# def natsum(n):
#     s=0
#     if(n==0):
#         return 0
#     s=n+s
#     return s+natsum(n-1)

# print("Sum of given natural number is: ",natsum(10))

# #factorial of number
# def factorial(n):
#     f=1
#     if(n==0 or n==1):
#         return 1
#     f=f*n       ## multiplying current number with saved sum value
#     return f*factorial(n-1) #reoccurance of the function working

# print("Factorial of given number is: ",factorial(5))

#fibonacci Series  0,1,1,2,3,5,8,13,....

def fib_series(n, a=0, b=1):
    if n > 0:
        print(a, end=", ")
        fib_series(n-1, b, a+b)  # Recursive call with updated values

print("Fibonacci Series up to 10 terms:")
fib_series(10)



    