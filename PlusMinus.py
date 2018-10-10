#Plus Minus
n=int(input())
inp=input()
arr=inp.split(' ')
sum1,sum2,sum3=0,0,0
for i in arr:
    if int(i)>0:
        sum1+=1
    elif int(i)<0:
        sum2+=1
    else:
        sum3+=1
sum4=int(sum1+sum2+sum3)
print(sum1/sum4)
print(sum2/sum4)
print(sum3/sum4)
