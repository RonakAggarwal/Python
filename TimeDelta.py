from datetime import datetime
t=int(input());
while t!=0:
    t1=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z');
    t2=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z');
    print(abs(int((t1-t2).total_seconds())));
    t=t-1;
