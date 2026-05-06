def is_valid_input(n:str):
    while '()' in n or '{}' in n or '[]' in n:
        n = n.replace('()','')
        n = n.replace('{}','')
        n = n.replace('[]','')
    if len(n) == 0: 
        return True
    else: 
        return False




if __name__ == '__main__':
    n = input()
    print(is_valid_input(n))
