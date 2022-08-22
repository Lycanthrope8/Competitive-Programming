T = int(input())
for i in range(T):
    n = int(input())

    ##making a list of integer from a string of numbers
    arr = list(map(int, input().split()))

    # creating dictionary to store the number of elememts showed in the array
    d = {}
    # Adjesccent will be False untill one element gets bigger that n/2
    adj = False
    for val in arr:
        if val not in d:
            d[val] = 0
        d[val] += 1
        m=n/2

        ## if n is 10 and and some element showed 6 times then 10-6+1<6. More than half of the Len
        if n-d[val]+1< d[val]:
            # print(d[val])

            # Adjecsent become true and loop breaks
            adj = True
            break
    if adj is True:
        print("NO")
    else:
        print("YES")