def list_of_evens(n):
    evens = []
    cnt = 0
    for i in range (2,n+1,2):
        evens.append(i)
        cnt += 1
        if cnt == 20:
            break
    return evens

def list_of_odds(n):
    count = 0 
    odds = []
    for i in range (1,n+1,2):
        odds.append(i)
        count += 1 
        if count == 20:
            break
    return odds

print (list_of_evens(80))
print (list_of_odds(80))