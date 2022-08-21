##Problem Link: https://www.codechef.com/SEPT21C/problems/PALINT

t = int(input())
for q in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = a;
    m = 0
    dic = {}
    original = {}
    # print('0')
    for i in range(n):
        b.append(a[i] ^ x)
        dic[a[i]] = 0
        dic[b[-1]] = 0
        original[a[i]] = 0
    for i in b:
        dic[i] += 1
        m = max(m, dic[i])
    for i in range(n):
        original[a[i]] += 1
    l = []
    for i in dic.keys():
        if dic[i] == m:
            # print(i)
            if i in original.keys():
                l.append(m - original[i])
            else:
                l.append(m)

    # print(dic)
    if x != 0:
        print(m, min(l))
    else:
        print(m // 2, 0)

