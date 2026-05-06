def del_to_find_a_same_word(n, m):
    cnt = [0] * 26
    cnt2 = [0] * 26
    
    del_from_n = []
    del_from_m = []
    

    for i in n:
        cnt[ord(i) - ord('a')] += 1
        

    for j in m:
        cnt2[ord(j) - ord('a')] += 1

    for i in range(26):
        if cnt[i] > cnt2[i]:
            diff = cnt[i] - cnt2[i]
            for _ in range(diff):
                del_from_n.append(chr(i + ord('a')))
                
        elif cnt[i] < cnt2[i]:
            diff = cnt2[i] - cnt[i]
            for _ in range(diff):
                del_from_m.append(chr(i + ord('a')))
                
    print(f"need to del from '{n}': {del_from_n}")
    print(f"need to del from '{m}': {del_from_m}")


if __name__ == '__main__':
    n = input()
    m = input()
    del_to_find_a_same_word(n, m)