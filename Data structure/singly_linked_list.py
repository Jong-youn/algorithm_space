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

  def addFirst(self, obj):
    new_node = Node(obj)
    new_node.next = self.head
    self.head = new_node

  def removeFirst(self):
    self.head = self.head.next

  def removeLast(self):
    last = self.head
    while last.next.next:
      last = last.next
    last.next = None

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

  def size(self):
    idx = 0
    search = self.head
    while search:
      search = search.next
      idx +=1
    return idx

a = LinkedList()
a.add(5)
a.addFirst(4)
ic(a.head.data, a.head.next.data)
a.add(10)
a.removeFirst()
ic(a.head.data) #5
a.add(15)
ic(a.contains(15))
ic(a.size())
a.removeLast()
ic(a.contains(15))
ic(a.size())

