def leftroation(STR1):
    A = list(STR1)
    temp=STR1
    for i in range(1,len(A)+1):
        A.append(A[0])
        A.remove(A[0])
        if ''.join(A)==temp:
            print(i)
            break

Str1 = input("Enter first String : ")
leftroation(Str1)