def anagram(STR1,STR2):
    A = STR1
    B = STR2
    AT = 1
    if len(A)-A.count(' ') == len(B)-B.count(' '):
        for i in list(A):
            if i in B and i!=' ':
              AT = 1
            else:
                AT = 0

        if AT==1:
            print("Anagram")
            return True
        else:
            print ("Not Anagarm")
            return False

    else:
        print("Not Anagram")
        return False





# Str1 = input("Enter first String : ")
# Str2 = input("Enter second String : ")

Str1 = "Funeral "
Str2 = "Real Fun"

anagram(Str1,Str2)