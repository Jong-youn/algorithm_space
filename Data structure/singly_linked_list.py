from icecream import ic

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList(object):
  def __init__(self):
    self.head = None

  def add(self, new):
    new_node = Node(new)

    if self.head:
      pointer = self.head
      while pointer.next:
        pointer = pointer.next
      pointer.next = new_node
    else:
      self.head = new_node

  def contains(self, obj):
    search = self.head
    while search:
      if search.data == obj:
        return True
      search = search.next
    return False

  def indexOf(self, obj):
    search = self.head
    idx = 0
    while search:
      if search.data == obj:
        return idx
      idx +=1
      search = search.next
    return -1

a = LinkedList()
# print(a, a.head)
a.add(5)
# print(a.head, a.head.data, a.head.next)
a.add(10)
# print(a.head, a.head.data, a.head.next)
a.add(15)
print(a.contains(15))
print(a.indexOf(15))