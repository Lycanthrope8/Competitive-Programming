# cook your dish here
T=int(input())

for i in range(T):
    n,m=input().split()
    ans= int(n)+int(m)
    if ans%2==0:
        print("Yes")
    else:
        print("No")

