
def sortBinArray(A1):
    ls=list(A1)

    min=ls[0]
    for i in range(0,len(ls)-1):
        for j in range(0,len(ls)-i-1):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1]=ls[j+1],ls[j]

    return ("".join(ls))





str1 = "10010"

print(sortBinArray(str1))
