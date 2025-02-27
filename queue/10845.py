#https://www.acmicpc.net/problem/10845

import sys

n=int(sys.stdin.readline().strip())
queue=[]
for i in range(n):
    command=list(sys.stdin.readline().strip().split())
    if command[0]=='push':
        queue.append(int(command[1]))

    elif command[0]=='front':
        print(-1) if len(queue)==0 else print(queue[0])
    
    elif command[0]=='back':
        print(-1) if len(queue)==0 else print(queue[-1])
    
    elif command[0]=='size':
        print(len(queue))
    
    elif command[0]=='empty':
        print(1) if len(queue)==0 else print(0)
    
    elif command[0]=='pop':
        if len(queue)!=0:
            print(queue[0])
            del queue[0]
        else:
            print(-1)