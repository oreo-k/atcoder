
a = list(map(int, input().split()))

num = ((a[0]*a[1]*a[2])-(a[3]*a[4]*a[5]))%998244353
print(num)