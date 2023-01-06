
n, x = map(int, input().split())
p = input().split()

for i, _p in enumerate(p):
    #print(i, _p)
    if int(_p) ==x:
        print(i+1)
        break