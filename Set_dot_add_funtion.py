def unique_stamp(arr):
    print(arr)
    numberofstamp = len(set(arr))
    return numberofstamp


if __name__ == '__main__':


    n = int(input())
    arr = [input() for x in range(n)]
    # arr = list(map(str,input().split()))
    result = unique_stamp(arr)
    print(result)
