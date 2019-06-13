n,m=map(int,input().split());
div=[x for x in range(1,int(n/2)) if n%x==0]
op=[]
for i in sorted(div,reverse=True):
    Sum=0;
    for j in range(1,m+1):
        Sum+=i*j;
        op.append(Sum);
        if Sum > n:
            break;
    if Sum==n:
        print(op);
        exit(0);
    op.clear();
print(-1);
