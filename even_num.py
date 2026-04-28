def list_of_evens(n):
    evens = []
    for i in range (2,n+1,2):
        evens.append(i)
    return evens

def list_of_odds(n):
    odds = []
    for i in range (1,n+1,2):
        odds.append(i)
    return odds

print (list_of_evens(10))
print (list_of_odds(10))