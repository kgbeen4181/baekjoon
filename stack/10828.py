#https://www.acmicpc.net/problem/10828

import sys

n=int(sys.stdin.readline().strip())
stack=[]
for i in range(n):
    command=list(sys.stdin.readline().strip().split())
    
    if command[0]=='push':
        stack.append(int(command[1]))
    
    elif command[0]=='pop':
        if len(stack)!=0:
            print(stack[-1])
            stack.pop()

        else:
            print(-1)

    elif command[0]=='size':
        print(len(stack))
    
    elif command[0]=='empty':
        print(1) if len(stack)==0 else print(0)
    
    elif command[0]=='top':
         print(stack[-1]) if len(stack)!=0 else print(-1)