n = int(input())
s = set(map(int, input().split()))
N = int(input())
functions = [input().split() for i in range (N)]

for a in functions:
    if a[0] == 'pop':
        s.pop()
    elif a[0] == 'discard':
        s.discard(int(a[1]))
    else:
        s.remove(int(a[1]))

print(sum(s))