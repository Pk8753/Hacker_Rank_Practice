def sumOfNumberInString(A1):
    Temp="0"
    Number_List = 0
    for i in A1:
        if (i.isdigit()):
            Temp += i
            print(Temp)
        else:
            Number_List+= int(Temp)
            print("Temp sum",Number_List)
            Temp="0"

    return  Number_List + int(Temp)

def find_sum(str1):
    temp = "0"
    Sum = 0
    for ch in str1:
        if (ch.isdigit()):
            temp += ch
        else:
            Sum += int(temp)
            temp = "0"
    return Sum + int(temp)





s1,s2= "1abc23","bbb5cc5dd12"
str1 = "12abc20yz68"

print(sumOfNumberInString(s1))
# print(find_sum(str1))