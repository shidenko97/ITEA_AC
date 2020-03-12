from collections import deque

q = deque()

q.append("eat")
q.append("sleep")
q.append("code")
q.appendleft("code")

q
# deque(['eat', 'sleep', 'code'])
q.popleft()
# 'code'
q.pop()
# 'sleep'
q.pop()
# 'eat'

q.pop()
