#https://www.acmicpc.net/problem/1874

n=int(input())
stack=[0]
save=[]
next_num=0
no_count=0
for i in range(n):
    num=int(input())
    for j in range(next_num+1,n+1):
        if stack[-1]==num:
            stack.pop()
            save.append('-')
            break
        else:
            stack.append(j)
            save.append('+')
            next_num=j
    if stack[-1]==num:
            stack.pop()
            save.append('-')
if len(stack)==1:
    for k in save:
        print(k)
else:
    print('NO')