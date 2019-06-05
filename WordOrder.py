# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n=int(input());
list=[];
for i in range(n):
    list.append(input());
c,d=0,0;
Dlist=[];
countList=[];
for i in list:
    if(i not in Dlist):
        if(list.count(i)==1):
            c=c+1;
            countList.append(list.count(i));
        else:
            c=c+1;
            countList.append(list.count(i));
            Dlist.append(i);

print(c);
for i in countList:
    print(i,end=' ');
