#https://www.acmicpc.net/problem/12605
n=int(input())
for i in range(1,n+1):
    stack = list(input().split())
    stack.reverse()
    print(f'Case #{i}: ',end='')
    for j in stack:
        print(j,end=' ')

