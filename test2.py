def del_to_find_a_same_word_no_counter(n, m):
    freq = {}
    

    for char in n:
        freq[char] = freq.get(char, 0) + 1
        

    for char in m:
        freq[char] = freq.get(char, 0) - 1
        
    del_from_n = []
    del_from_m = []
    

    for char in freq:
        count = freq[char]
        if count > 0:
            del_from_n.append([char] * count)
        elif count < 0:
            del_from_m.append([char] * abs(count))
            
    print(f"need to del from '{n}': {del_from_n}")
    print(f"need to del from '{m}': {del_from_m}")

if __name__ == '__main__':
    n = input()
    m = input()
    del_to_find_a_same_word_no_counter(n, m)