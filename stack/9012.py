#https://www.acmicpc.net/problem/9012

n=int(input())

for i in range(n):
    stack=[]
    wrong=0
    d=list(input())

    for j in d:
        if j=='(':
            stack.append(j)

        else:
            if len(stack)!=0:
                stack.pop()

            else:
                wrong+=1
    if wrong==0 and len(stack)==0:
        print('YES')
        
    else:
        print('NO')