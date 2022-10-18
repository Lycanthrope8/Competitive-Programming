###Link: https://codeforces.com/problemset/problem/1741/A

### T shirt size compare
S=1
M=2
L=3
T=int(input())
for i in range(T):
    inp = list(map(str,input().upper().split()))
    item1=inp[0]
    item2=inp[1]
    if item1[-1]=="M" or item2[-1]=="M":
        if item2[-1]=="L":
            print("<")
        elif item2[-1]=="S":
            print(">")
        elif item1[-1]=="L":
            print(">")
        elif item1[-1]=="S":
            print("<")
        else:
            print("=")
    else:
        if item1[-1]=="S":
            if item2[-1]=="S":
                if len(item1) == len(item2):
                    print("=")
                elif len(item1)<len(item2):
                    print(">")
                else:
                    print("<")
            else:
                print("<")
        else:
            if item2[-1]=="L":
                if len(item1) < len(item2):
                    print("<")
                elif len(item1)>len(item2):
                    print(">")
                else:
                    print("=")
            else:
                print(">")




