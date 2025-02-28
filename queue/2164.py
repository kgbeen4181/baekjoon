#https://www.acmicpc.net/problem/2164
#지우거나 추가하면 O(n^2)의 시간복잡도가 발생한다. ㅇㅇ...

import sys
from collections import deque
n=int(sys.stdin.readline().strip())
queue=deque([i for i in range(1,n+1)])

for j in range(n-1):
    queue.popleft()
    queue.append(queue.popleft())
print(queue[0])