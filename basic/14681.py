#https://www.acmicpc.net/problem/14681

x=int(input())
y=int(input())
print(1) if x>0 and y>0 else 0
print(2) if x<0 and y>0 else 0
print(3) if x<0 and y<0 else 0
print(4) if x>0 and y<0 else 0
