def order(s):
    meta=s
    occ={}
    for i in meta:
        if i not in occ:
            occ[i]=meta.count(i)
            print(occ)
        else:
            continue
    print(len(occ))
    print(*occ.values())

s=['bcdef','abcdefg','bcde','bcdef']

order(s)



############################################

# from collections import Counter
# n=int(input())
# l1=list()
# for i in range(n):
#     l1.append(input())
# x=Counter(l1)
# print(len(x))
# print(*x.values())