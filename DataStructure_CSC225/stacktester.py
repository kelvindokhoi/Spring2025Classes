# stacktester.py

import stack

s = stack.Stack()
try:
    print(s.isEmpty())
    for i in range(10):
        s.push(i)
    print(s.peek())
    while not s.isEmpty():
        print(s.pop(),s.getSize())
except ValueError:
    print('invalid ops')


