
import sys
h, w = map(int, input().split())

s = []
t = []

for _ in range(h):
    s.append(input())

for _ in range(h):
    t.append(input())

#print(s, t)
t_cols = []
s_cols = []
for i in range(w):
    _t_cols=[]
    _s_cols=[]
    for j in range(h):
        _t_cols.append(t[j][i])
        _s_cols.append(s[j][i])
        #print("_t_cols:{}".format(_t_cols))
    t_cols.append(_t_cols)
    s_cols.append(_s_cols)


t_cols.sort()
s_cols.sort()

if t_cols == s_cols:
    print("Yes")
else:
    print("No")