#https://www.acmicpc.net/problem/9498
n=int(input())
print('A') if n>=90 and n<=100 else 0
print('B') if n>=80 and n<=89 else 0
print('C') if n>=70 and n<=79 else 0
print('D') if n>=60 and n<=69 else 0
print('F') if n<=59 else 0