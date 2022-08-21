##Problem Link: https://www.codechef.com/SEPT21C/problems/SHUFFLIN
t=int(input())
i=0
for x in range(t):
    out=0
    n=int(input())
    even=0
    odd=0
    arraystr = input().split()[:n]
    arraystr = list(map(int, arraystr))

    for i in arraystr:
        if i%2==1:
            odd+=1
        else:
            even+=1
    evenover=(n+1)//2
    oddover=n//2
    if evenover>even:
        out+=even
    else:
        out+=evenover
    if oddover>odd:
        out+=odd
    else:
        out+=oddover
    print(out)