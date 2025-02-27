#https://www.acmicpc.net/problem/12605
#이건 스택으로 푼 게 아닌 거 같다. ㅇㅇ....

n=int(input())

for i in range(1,n+1):
    stack = list(input().split())
    stack.reverse()
    print(f'Case #{i}: ',end='')

    for j in stack:
        print(j,end=' ')

