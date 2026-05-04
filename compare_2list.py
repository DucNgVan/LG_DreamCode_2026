def count_2list(n, m):

    count_1 = [0] * 52
    count_2 = [0] * 52
    

    for i in n:
        if i.islower():
            count_1[ord(i) - ord('a')] += 1
        elif i.isupper():
            count_1[ord(i) - ord('A') + 26] += 1

    for i in m: 
        if i.islower():
            count_2[ord(i) - ord('a')] += 1
        elif i.isupper():
            count_2[ord(i) - ord('A') + 26] += 1
            

    for i in range(52):
        if count_1[i] != count_2[i]:
            return False
    return True

if __name__ == '__main__':
    n = input().split(',')
    m = input().split(',')
    print(count_2list(n, m))