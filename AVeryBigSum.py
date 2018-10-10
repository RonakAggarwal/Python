#A very big sum
n=int(input())
items=input()
integer=items.split(' ')
sum=0
for i in range(0,n):
    temp=int(integer[i])
    sum+=temp
print(sum)
    