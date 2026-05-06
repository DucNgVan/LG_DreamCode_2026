a = ['a','b','c',5,7.6,True,'c']
b = ['a','c',5,7.6,True,'b','b']

if len(a) > len(b) or len(b) > len(a):
    print('False')
else:
    ans_a={}
    ans_b={}

    for i in a:
        if i not in ans_a:
            ans_a[i] = 1
        else:
            ans_a[i] += 1
    for j in b:
        if j not in ans_b:
            ans_b[j] = 1
        else:
            ans_b[j] += 1

    print(ans_a == ans_b)