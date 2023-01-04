h, m = map(int, input().split())
#h=1
#m=23

flag = False
def judge(h,m):
    h = str("%02d" %h)
    m = str("%02d" %m)

    _h = int(h[0]+m[0])
    _m = int(h[1]+m[1])

    if (_h<=23) and (_m<=59):
        flag=True
        return [int(h), int(m)]

    else:
        return [0] 

while flag ==False:
    
    h = h%24
    m = m%60
    judgement = (judge(h,m))
    if len(judgement)==1:
        m+=1

        if m%60==0:
            h+=1
    else:
        flag=True
        print(judgement[0], judgement[1])


