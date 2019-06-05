import math
t=int(input());
while t>0:
    input();
    list=input().split(" ");
    i=0;
    j=len(list)-1;
    n=math.inf;
    while(i<j):
        ans=1;
        if(int(list[i])>=int(list[j]) and int(list[i])<=n):
            n=int(list[i]);
            i+=1;
        elif int(list[j])>int(list[i]) and int(list[j])<=n:
            n = int(list[j]);
            j -= 1;
        else:
            ans=0
            break;
    if ans==0:
        print("No");
    else:
        print("Yes");
    t-=1;


