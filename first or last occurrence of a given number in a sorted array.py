def firstAndLastOccuranceSortedArray(arr,target):
    firstOccurance,lastOccurance = 0,0
    for index,val in enumerate(arr):
        if val == target:
            firstOccurance = index
            lastOccurance = firstOccurance + arr.count(target) - 1
            break
    print("first occurance =", firstOccurance)
    print("last occurance = ", lastOccurance)



def firstAndLastOccuranceUnSortedArray(arr,traget):
    firstOccurance,lastOccurance = 0,0
    for index,val in enumerate(arr):
        if firstOccurance == 0 and lastOccurance == 0 and val == target:
            firstOccurance = index

        elif val == target:
            lastOccurance =  index

        else:
            continue

    print("first occurance =", firstOccurance)
    print("last occurance = ", lastOccurance)





sArr = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9] #Sorted Array
UnsArr = [2, 5, 3, 2, 5, 8, 9, 5, 6, 3]
target = 5                           #a number whose occuranace

# firstAndLastOccuranceSortedArray(sArr,target) #1,3

firstAndLastOccuranceUnSortedArray(UnsArr,target) #1,7