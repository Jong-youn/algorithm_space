from icecream import ic

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList(object):
  def __init__(self):
    self.head = None

  # 리스트의 가장 마지막에 데이터 추가
  def add(self, new):
    new_node = Node(new)

    if self.head:
      pointer = self.head
      while pointer.next:
        pointer = pointer.next
      pointer.next = new_node
    else:
      self.head = new_node

  # 리스트의 가장 첫번째 인덱스에 데이터 추가
  def addFirst(self, obj):
    new_node = Node(obj)
    new_node.next = self.head
    self.head = new_node

  # 특정 인덱스에 있는 데이터 제거. 매개변수가 없을 시 맨 처음 인덱스를 삭제한다.
  def remove(self, obj=0):
    if obj < 0 or obj >= self.size():
      print('\033[31m' + 'Error :: 적절하지 않은 입력 값 입니다.')
      return 
    elif obj == 0:
      self.removeFirst()
    else:
      search = self.head
      idx = 0
      while search.next:
        if idx == (obj-1):
          before = search
        elif idx == obj:
          break
        search = search.next
        idx +=1
      before.next = search.next

  # 리스트의 가장 첫번째 값 삭제
  def removeFirst(self):
    self.head = self.head.next

  # 리스트의 가장 마지막 값 삭제
  def removeLast(self):
    last = self.head
    while last.next.next:
      last = last.next
    last.next = None

  # 리스트가 특정 데이터를 포함하고 있는지 여부
  def contains(self, obj):
    search = self.head
    while search:
      if search.data == obj:
        return True
      search = search.next
    return False

  # 특정 데이터의 위치 값 출력, 없으면 -1 반환 
  # 같은 데이터를 여러개 포함하고 있다면, 리스트의 제일 앞에 위치한 위치를 출력
  def indexOf(self, obj):
    search = self.head
    idx = 0
    while search:
      if search.data == obj:
        return idx
      idx +=1
      search = search.next
    return -1

  # 링크드 리스트의 총 길이 
  def size(self):
    idx = 0
    search = self.head
    while search:
      search = search.next
      idx +=1
    return idx

a = LinkedList()
a.add(5)
ic(a.head)
a.remove(0)
ic(a.head)
a.remove(-1)
a.add(5)
a.remove()
a.add(6)
a.add(7)
a.add(8)
a.add(9)
a.remove(1)
print(a.contains(6))
ic(a.head.data, a.head.next.data)
a.addFirst(4)
ic(a.head.data)
a.add(10)
a.removeFirst()
ic(a.head.data) #5
a.add(15)
ic(a.contains(15))
ic(a.size())
a.removeLast()
ic(a.contains(15))
ic(a.size())

