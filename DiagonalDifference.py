#Diagonal Difference
import math
n=int(input())
matrix=[]
sum1,sum2=0,0
for i in range(n):
    rows=input()
    arr=rows.split(' ')
    sum1+=int(arr[i]);
    sum2+=int(arr[n-i-1])
print(abs(sum1-sum2))