
n = int(input())

h = list(map(int, input().split()))
#print(h)
max_num = 0
for i in range(len(h)):
    num = h[i]
    if max_num < num:
        max_num = num
        max_ind = i

print(max_ind+1)
