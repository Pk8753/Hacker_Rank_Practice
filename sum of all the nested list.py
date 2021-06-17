def sum(test):
    total = 0
    for i in test:
        if str(i).isdigit():
            total=total + i
        else:
            sum(i)
    return total




test = [4, 4, [47, 48], 3, 6, [4, 6, 4, 3, [4, 5, 3], 52], 454]
t= sum(test)
print(t)