def factorial(s):
    ans = 1
    if s == 1:
        print (1)
    else:
        for i in range(1,s+1):
            ans = ans * i
        print(ans)


if __name__ == '__main__':
    s = int(input())
    factorial(s)
