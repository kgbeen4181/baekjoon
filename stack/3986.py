#https://www.acmicpc.net/problem/3986

n=int(input())
good=0
for i in range(n):
    stack=[]
    word=list(input())

    for j in word:
        if len(stack)!=0 and stack[-1]==j:
            stack.pop()

        else:
            stack.append(j)
            
    if len(stack)==0:
        good+=1
print(good)