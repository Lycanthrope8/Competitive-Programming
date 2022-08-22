T=int(input())
for i in range(T):
    n=[]
    N=int(input())
    for i in range(1,N+1):
        n.append(i)
    n.reverse()
    for i in n:
        print(i,end=" ")

