#Time Conversion
n=input()
p=n[:-2]
q=n[-2]+n[-1]
time=p.split(':')
if time[0]=="12":
    if q=="AM":
        temp=int(time[0])
        temp=(temp+12)%24
        if temp==0:
            time[0]="00"
        else:
            time[0]=str(temp)
elif q=="PM" and time[0]!="12":
    temp=int(time[0])
    temp=(temp+12)%24
    time[0]=str(temp)
a=':'.join(time)
print(a)
