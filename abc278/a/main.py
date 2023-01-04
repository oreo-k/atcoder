n, k = map(int, input().split())

a = input().split()

for i in range(k):
    a.pop(0)
    a.append(0)

for i in range(len(a)):
    if i!=len(a)-1:
        print(a[i], end=" ")
    else:
        print(a[i])