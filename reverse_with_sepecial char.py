def reverse_char(n):
    l = list(n)
    temp=''
    k={}
    count=0
    for i in l:
        if str(i).isalpha():
            temp =str(i)+ temp
        else:
            if (i != ' '):
                k[i]=len(temp)+count
                count=count+1
            else:
                continue
    # print(k)
    temp=list(temp)
    for j in k:
        count=-1
        if(j!=' '):
            count=count + 1
            temp.insert((k[j]),j)
            # print((k[j]+count),j)
    print(''.join(temp))




n = 'it\'s my life!'
m='I Am Groot!'
# print(n)
reverse_char(n)
reverse_char(m)
