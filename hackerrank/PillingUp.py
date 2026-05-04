

def is_pilling_up(m):
    i = 0
    j = len(m)-1
    n = 'Yes'
    last_picked = max(m)
    while i < j:
        if m[i] >= m[j]:
            current = m[i]
            i += 1
            print(current)
        else:
            current = m[j]
            j -= 1
            print(current)
        if current > last_picked:
            print('No')
            return
        last_picked = current
    print(n)


turn = int(input())
for i in range(turn):
    n = int(input())
    m = list(map(int,input().split()))
    is_pilling_up(m)