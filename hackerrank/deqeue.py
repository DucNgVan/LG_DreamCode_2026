from collections import deque

n = int(input())
d = deque()

for _ in range(n):
    line = input().split()
    command = line[0]
    
    if command == 'append':
        d.append(line[1])
    elif command == 'appendleft':
        d.appendleft(line[1])
    elif command == 'pop':
        d.pop()
    elif command == 'popleft':
        d.popleft()

print(*(d))