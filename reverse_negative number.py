def reverse_number(n):
    input_data = str(n)
    if (input_data[0]=='-'):
        test_data = input_data[1:]
        print('-'+test_data[::-1])
    else:
        test_data = input_data[::-1]
        if (test_data[0]=='0'):
            print(test_data[1:])
        else:
            print(test_data)



n = "-1245"
m = "0134"
reverse_number(n)
reverse_number(m)
