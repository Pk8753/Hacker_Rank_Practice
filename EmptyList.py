from collections import Counter
n=int(input())
l1=list()
for i in range(n):
    l1.append(input())
x=Counter(l1)

print(len(x))
print(*x.values())