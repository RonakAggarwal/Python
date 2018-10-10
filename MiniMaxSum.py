#Mini-Max Sum
n=input()
a=n.split(' ')
b=sorted(a)
sum1,sum2=0,0
for i in range(5):
    if i==0:
        sum1+=int(b[i])
    elif i==4:
        sum2+=int(b[i])
    else:
        sum1+=int(b[i])
        sum2+=int(b[i])
print(sum1,sum2)