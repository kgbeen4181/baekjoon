#https://www.acmicpc.net/problem/10773

n=int(input())
stack=[]
for i in range(n):
    num=int(input())
    if num==0:
        stack.pop()
    else:
        stack.append(num)

if len(stack)==0:
    print(0)
else:
    print(sum(stack))