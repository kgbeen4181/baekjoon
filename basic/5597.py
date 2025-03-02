#https://www.acmicpc.net/problem/5597

order=[i for i in range(1,31)]
for i in range(28):
    n=int(input())
    order.remove(n)
print(min(order))
print(max(order))