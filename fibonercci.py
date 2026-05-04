def fibonacci(n): 
    a, b = 0 , 1
    ans =[]
    for i in range(n):
        ans.append(a)
        a, b = b, a+b
    return ans

if __name__ == '__main__':
    n = int(input())
    print(fibonacci(n))



