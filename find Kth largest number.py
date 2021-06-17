def kthlargest(a,k):
    for i in range(1,k):
        a.remove(max(a))

    print (str(k) + " largest number is " + str(max(a)))





arr = [5,4,6,7,2,3,1]

K = int(input("Enter value to find which largest number you wana search : "))

kthlargest (arr,K)