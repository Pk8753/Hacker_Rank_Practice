def find (l,x):
    for i in l:
        if i.startswith(x):
            print (i)
        else :
            continue






list1 = ["door","dog","cat","file","dorge"]
se = input("Enter search text : ")
find(list1,se)