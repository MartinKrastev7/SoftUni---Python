class Stack:
    def __init__(self):
        self.values = []

    def push(self, value):
        self.values.append(value)

    def pop(self):
        return self.values.pop()

    def peek(self):
        return self.values[-1]

    def count(self):
        return len(self.values)


s = Stack()

for v in range(5, 10):
    s.push(v)

print(s.pop())
print(s.peek())
print(s.count())
#class za stack

#zadacha 1
#original_string[::-1]
#original_string.reverse()
original_string = input()

s = []
for c in original_string:
    #push into stack
    s.append(c)

reversed_string = ""
while s:
    value = s[-1] # peek
    reversed_string += value
    s.pop() # pop

print(reversed_string)