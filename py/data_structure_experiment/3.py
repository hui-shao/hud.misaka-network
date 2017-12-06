print("1: std list")
std_li = []
print("insert a, b, c, d, e")
temp1 = {
    "a": 1, "b": 2,
    "c": 3, "d": 4,
    "e": 5
}
for i in temp1:
    std_li += [temp1[i]]

print("print table")
print(std_li)
print("print table length")
print(len(std_li))
print("is empty")
print(len(std_li) == 0)
print("3rd element")
print(std_li[2])
print("location of element a")
for i in range(0, len(std_li)):
    if std_li[i] == 1:
        print(i)
print("insert element f at 4")
std_li = std_li[0:3] + [6] + std_li[4:]
print("print table")
print(std_li)
print("delete 3rd elem")
del std_li[3]
print("print table")
print(std_li)
print("release table")
del std_li

print("2: std link list")
pointerSto = []
print("insert a, b, c, d, e")
temp2 = {
    "a": 1, "b": 2,
    "c": 3, "d": 4,
    "e": 5
}
for i in temp2:
    pointerNewSto = pointerSto + [temp2[i]]
    pointerSto = pointerNewSto
    del pointerNewSto

print("print table")
print(pointerSto)
print("print table length")
print(len(pointerSto))
print("make sure if the table is empty")
if len(pointerSto):
    print("the table is not empty")
else:
    print("the table is empty")
print("print 3rd element in the table")
print(pointerSto[2])
print("print the location of the element a")
for i in range(0, len(pointerSto)):
    if pointerSto[i] == 1:
        print(i)
print("insert f")
f = 6
pointerNewSto = pointerSto[0:2] + [f] + pointerSto[3:]
pointerSto = pointerNewSto
del pointerNewSto
print("print table")
print(pointerSto)
print("del 3rd element of table")
del pointerSto[2]
print("print table")
print(pointerSto)
print("release table")
del pointerSto


class Node(object):
    def __init__(self, val, p=0):
        self.data = val
        self.next = p


class LinkList(object):
    def __init__(self):
        self.head = 0

    def __getitem__(self, key):

        if self.is_empty():
            print('linklist is empty.')
            return

        elif key < 0 or key > self.getlength():
            print('the given key is error')
            return

        else:
            return self.getitem(key)

    def __setitem__(self, key, value):

        if self.is_empty():
            print('linklist is empty.')
            return

        elif key < 0 or key > self.getlength():
            print('the given key is error')
            return

        else:
            self.delete(key)
            return self.insert(key)

    def initlist(self, data):

        self.head = Node(data[0])

        p = self.head

        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next

    def getlength(self):

        p = self.head
        length = 0
        while p != 0:
            length += 1
            p = p.next

        return length

    def is_empty(self):

        if self.getlength() == 0:
            return True
        else:
            return False

    def clear(self):

        self.head = 0

    def append(self, item):

        q = Node(item)
        if self.head == 0:
            self.head = q
        else:
            p = self.head
            while p.next != 0:
                p = p.next
            p.next = q

    def getitem(self, index):

        if self.is_empty():
            print('Linklist is empty.')
            return
        j = 0
        p = self.head

        while p.next != 0 and j < index:
            p = p.next
            j += 1

        if j == index:
            return p.data

        else:

            print('target is not exist!')

    def insert(self, index, item):

        if self.is_empty() or index < 0 or index > self.getlength():
            print('Linklist is empty.')
            return

        if index == 0:
            q = self.head.next

            self.head = q

        p = self.head
        post = self.head
        j = 0
        while p.next != 0 and j < index:
            post = p
            p = p.next
            j += 1

        if index == j:
            q = Node(item, p)
            post.next = q
            q.next = p

    def delete(self, index):

        if self.is_empty() or index < 0 or index > self.getlength():
            print('Linklist is empty.')
            return

        if index == 0:
            q = self.head.next

            self.head = q

        p = self.head
        post = self.head
        j = 0
        while p.next != 0 and j < index:
            post = p
            p = p.next
            j += 1

        if index == j:
            post.next = p.next

    def index(self, value):

        if self.is_empty():
            print('Linklist is empty.')
            return

        p = self.head
        i = 0
        while p.next != 0 and not p.data == value:
            p = p.next
            i += 1

        if p.data == value:
            return i
        else:
            return -1


print("3: round list")
li = []
print("insert a, b, c, d, e")
temp1 = {
    "a": 1, "b": 2,
    "c": 3, "d": 4,
    "e": 5
}
for i in temp1:
    li += [temp1[i]]

print("print table")
print(li)
print("print table length")
print(len(li))
print("is empty")
print(len(li) == 0)
print("3rd element")
print(li[2])
print("location of element a")
for i in range(0, len(li)):
    if li[i] == 1:
        print(i)
print("insert element f at 4")
li = li[0:3] + [6] + li[4:]
print("print table")
print(li)
print("delete 3rd elem")
del li[3]
print("print table")
print(li)
print("release table")
del li
