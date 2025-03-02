typing=list(input())
n=int(input())
now_cursor=len(typing)
for i in range(n):
    command=list(input().split())
    if command[0]=='P':
        typing.insert(now_cursor,command[1])
    if command[0]=='D':
        if now_cursor>=1:
            now_cursor-=1
    if command[0]=='L':
        if now_cursor<len(typing):
            now_cursor+=1
    if command[0]=='B':
        typing.pop()
        #수정해야됨