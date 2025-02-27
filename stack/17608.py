#https://www.acmicpc.net/problem/17608

import sys

n = int(sys.stdin.readline().strip())
stack=[]
order = [int(sys.stdin.readline().strip()) for i in range(n)]
for num in reversed(order):
    if len(stack)==0 or num>stack[-1]:
        stack.append(num)
print(len(stack))
