class Queue:
  def __init__(self, arr=[]):
    self.queue = arr
  def enqueue(self, data):
    self.queue.append(data)
    print(self.queue)
  def dequeue(self):
    print(self.queue.pop(0))
  def print(self):
    print(self.queue)

class Stack:
  def __init__(self, arr=[]):
    self.stack = arr
  def push(self, data):
    self.stack.append(data)
    print(self.stack)
  def pop(self):
    print(self.stack.pop(-1))
  def print(self):
    print(self.stack)

print('Creating stack')
stack = Stack([10,20,30])
stack.print()
print('Push operation - adding 40')
stack.push(40)
print('Push operation - adding 50')
stack.push(50)
print('Pop operation')
stack.pop()

print('Creating queue')
q = Queue([-10,20,30])
q.print()
print("Enqueue - 40")
q.enqueue(40)
print("Dequeue")
q.dequeue()
