n, d = map(int, input().split())

times = [int(time) for time in input().split()]
flag_dd = False
pre_time = times[0]
for time in times[1:]:
  if time-pre_time <=d:
    print(time)
    flag_dd = True 
    break
  else:
    pre_time = time
if flag_dd==False:
  print(int(-1))
    
