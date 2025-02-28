# n,k=map(int,input().split())
# queue=[i for i in range(1,n+1)]
# order=0
# count=0
# print('<',end="")
# for i in range(1,n+1):
#     if count==0:
#         order=order+k-1
#     else:
#         order+=k
#     if order>=n:
#         order-=n
#     if count==6:
#         print(f'{queue[order]}',end='')
#     else:
#         print(f'{queue[order]}, ',end='')
#     count+=1
#     if count==7:
#         break
# print('>',end='')
#
#문제 이해 이슈로 다음에 고칠 예정정