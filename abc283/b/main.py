
n = int(input())
a = list(map(int,input().split()))

num_q = int(input())
for q in range(num_q):
    _q = list(map(int,input().split()))

    if len(_q)==3:
        k = _q[1]
        x = _q[2]
        a[k-1]=x

    elif len(_q)==2:
        k=_q[1]
        print(a[k-1])
