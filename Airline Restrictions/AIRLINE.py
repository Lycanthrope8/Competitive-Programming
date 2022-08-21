##Problem Link: https://www.codechef.com/SEPT21C/problems/AIRLINE

# cook your dish here
def response(a,b,c,d,e):
    if a+b<=d and c<=e:
        return "YES"

    elif a+c<=d and b<=e:
        return "YES"

    elif b+c<=d and a<=e:
        return "YES"

    else:
        return "NO"

limit=int(input())

for i in range(limit):
    user=input().split(" ")
    a,b,c,d,e=user
    print(response(int(a),int(b),int(c),int(d),int(e)))

