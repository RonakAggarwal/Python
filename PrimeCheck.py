#program to check whether a number is prime or not
import math
n=int(input())
ch=0
for i in range(2,math.floor(math.sqrt(n))+1):
    if(n%i==0):
        ch=1
if ch==0:
    print("number is prime")
else:
    print("number is not prime")
        
    