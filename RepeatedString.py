#Repeated String
import math
str=input()
countA=str.count('a')
n=int(input())
count=countA*(math.floor(n/len(str)))
for i in range(n%len(str)):
    if str[i]=='a':
        count+=1
print(count)