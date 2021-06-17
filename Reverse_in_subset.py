def reverseInSubset(a,s):
    finalList = []
    for i in range (0,len(a),s):
        k = (a[i:i+s])
        k.reverse()
        finalList.append(k)
        flatten_list = [j for sub in finalList for j in sub]
    print(flatten_list)




Arraylist = [1,3,5,7,9,11,15,17,19]
Subset = 3

reverseInSubset(Arraylist,Subset)