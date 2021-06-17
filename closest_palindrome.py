# Python3 program to find the
# closest Palindrome number
 
# Function to check Palindrome
 
 
def isPalindrome(n):
    for i in range(len(n) // 2):
        if (n[i] != n[-1 - i]):
            return False
    return True
 
# Function return closest Palindrome number
 
 
def closestPalindrome(num):
 
    # Case1 : largest palindrome number
    # which is smaller than given number
    RPNum = num - 1
    while (not isPalindrome(str((RPNum)))):
        RPNum -= 1
 
    # Case2 : smallest palindrome number
    # which is greater than given number
    SPNum = num + 1
    while (not isPalindrome(str(SPNum))):
        SPNum += 1
 
    # Check absolute difference
    if (abs(num - RPNum) > abs(num - SPNum)):
        return SPNum
    else:
        return RPNum
 
 
# # Driver Code
# if __name__ == '__main__':
#
#     num = 150
#
#     print(closestPalindrome(num))
#     #print(isPalindrome(str(num)))
#
