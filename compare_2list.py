def count_2list(n,m):
    count_1 = [0] * 26
    count_2 = [0] * 26
    for i in n: 
        count_1[ord(i)-ord('a')] += 1
    for i in m: 
        count_2[ord(i)-ord('a')] += 1
    for i in range(26):
        if count_1[i] != count_2[i]:
            return False
    return True

if __name__ == '__main__':
    n = list(map(str,input().split(',')))
    m = list(map(str,input().split(',')))
    print(count_2list(n,m))