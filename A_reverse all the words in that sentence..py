def reverseAll(A1):
    reverse = ""
    ls= A1.split(" ")
    for i in ls:
        reverse =reverse + i[::-1] +" "
    return (reverse)





str1 = "This is sample text"

print(str1)
print(reverseAll(str1))