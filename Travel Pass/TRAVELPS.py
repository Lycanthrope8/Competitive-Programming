#Problem Link: https://www.codechef.com/SEPT21C/problems/TRAVELPS

# cook your dish here
def timecalc(a,b,distrct,state):
    result=(distrct*int(a))+(state*int(b))
    return result

limit=int(input())

for i in range(limit):
    time=input().split()
    n,a,b=time
    dis=input()[:int(n)]
    district = 0
    state = 0
    for i in dis:
        if i=="0":
            district+=1
        if i=="1":
            state+=1
    print(timecalc(a,b,district,state))