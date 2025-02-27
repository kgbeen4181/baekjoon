#https://www.acmicpc.net/problem/28278
import sys

n=int(sys.stdin.readline().strip())
stack=[]
for i in range(n):
    num=list(map(int,sys.stdin.readline().strip().split()))
    if num[0]==1:
        stack.append(num[1])
    elif num[0]==2:
        if len(stack)!=0:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
    elif num[0]==3:
        print(len(stack))
    elif num[0]==4:
        print(1) if len(stack)==0 else print(0)
    elif num[0]==5:
        print(stack[-1]) if len(stack)!=0 else print(-1)
