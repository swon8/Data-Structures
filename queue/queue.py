class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    self.next_node = new_next


class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, value):
    new_node = Node(value)
    if not self.head and not self.tail:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.set_next(new_node)
      self.tail = new_node

  def remove_head(self):
    if not self.head and not self.tail:
      return None
    if self.head == self.tail:
      head = self.head
      self.head = None
      self.tail = None
      return head.get_value()
    else:
      old_head = self.head
      self.head = self.head.get_next()
      return old_head.get_value()

  def return_head(self):
    if self.head:
      return self.head.get_value()
    else:
      return None

  def return_tail(self):
    if self.tail:
      return self.tail.get_value()
    else:
      return None

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_tail(item)
    self.size += 1

  def dequeue(self):
    if self.size > 0:
      old_head = self.storage.head.get_value()
      self.storage.remove_head()
      self.size -= 1
      return old_head
    else:
      return None

  def len(self):
    return self.size

  def __str__(self):
    return f'head: {self.storage.return_head()}, tail: {self.storage.return_tail()}, length: {self.size}'


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
#q.dequeue()
print(q)