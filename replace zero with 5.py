
def replaceZeroWithFive(a):

   ls = [int(x) for x in str(a)]
   count = 0
   for i in ls:
       if i == 0 :
           ls[count] = 5
       count = count + 1

   st =[str(k) for k in ls]
   O = int("".join(st))
   print (O)
replaceZeroWithFive(100058475390345384030)