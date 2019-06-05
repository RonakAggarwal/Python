# Enter your code here. Read input from STDIN. Print output to STDOUT
m,n=tuple(map(int,raw_input().split()))
arr=list(map(int,raw_input().split()))
A=set(map(int,raw_input().split()))
B=set(map(int,raw_input().split()))
happy=len([x for x in arr if x in A])
sad=len([i for i in arr if i in B])
print happy-sad
