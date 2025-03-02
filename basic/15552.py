#https://www.acmicpc.net/problem/15552

import sys

n=int(sys.stdin.readline().strip())
for i in range(n):
    a,b=map(int,sys.stdin.readline().strip().split())
    print(a+b)
