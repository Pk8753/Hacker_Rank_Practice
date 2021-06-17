def DuplicateFind(A1):
    for index,val in enumerate(A1):
        if val == A1[index + 1] and val == A1[index]:
            print(val)
            break
        else:
            continue






list1 = [2, 5, 2, 4, 1, 3, 7, 5, 5, 2]

print(DuplicateFind(list1))