n = int(input())
s=[]
for _n in range(n):
    s.append(input())
for i in range(n):
    print(s[-1*(i+1)])
    