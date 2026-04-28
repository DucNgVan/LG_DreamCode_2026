
def fizz_buzz(n):
    for i in range (1,n+1): 
        if i % 15 == 0: 
            message = "FizzBuzz"
            print (message)
        elif i % 3 == 0: 
            print ("Fizz")
        elif i % 5 == 0: 
            print ("Buzz")
        else: 
            print (i)

# import time 
# def fizz_buzz_2(n,i=1): 
#     if i > n: 
#         return
    
#     if i % 15 == 0: 
#         print ("FizzBuzz")
#     elif i % 3 == 0: 
#         print ("Fizz")
#     elif i % 5 == 0: 
#         print ("Buzz")
#     else: 
#         print (i)

#     fizz_buzz_2(n,i+1)

n = input()
fizz_buzz(int(n))
# fizz_buzz_2(int(n)))