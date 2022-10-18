## Link: https://codeforces.com/problemset/problem/144/A?

n=int(input())
line=list(map(int,input().split()))
max_value = max(line)
min_value = min(line)
max_index = 0 #line.index(max_value)
min_index = 0 #line.index(min_value)
for i in range(len(line)):
    if line[i]==max_value:
        max_index=i
        # print(i)
        break
for i in range(len(line)):
    if line[i]==min_value:
        min_index=i
time=0
# print(max_index,min_index)
if max_index<min_index:
    time=(max_index-1)+(n-min_index)
if max_index>min_index:
    time=(max_index-1)+(n-min_index)-1

print(time)