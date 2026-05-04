if __name__ == '__main__':
    n = int(input())
    result = [] 
    for i in range(n):
        name = input().split()
        result.append(name)

    name= input()
    for i in range(len(result)):
        if result[i][0] == name:
            ans = 0 
            for x in result[i][1:]:
                x = float(x)
                ans += x
            avg = ans / len(result[i][1:])
            print("{:.2f}".format(avg))
            break