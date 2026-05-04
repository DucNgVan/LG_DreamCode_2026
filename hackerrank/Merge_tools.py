def merge_the_tools(string, k):
    cnt = 0 
    ans = []
    len_ans = len(string) // k
    for i in string:
        if i not in ans: 
            ans.append(i)
            cnt += 1 
        else: 
            cnt += 1 
        if cnt == k:
            print(''.join(map(str, ans)))
            ans = []
            cnt = 0
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)