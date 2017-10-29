print("Page 117 / 1")


class UserStack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False

    def call_is_empty(self):
        print("call is_empty")
        print(self.is_empty())

    def push(self, element):
        self.stack += [element]

    def pop(self):
        elem = self.stack[-1]
        del self.stack[-1]
        return elem


print("stack initialize")
stack1 = UserStack()

stack1.call_is_empty()

print("push a, b, c, d, e")
sto1 = {"a": 1, "b": 4, "c": 5, "d": 1, "e": 4}
for i in sto1:
    stack1.push(sto1[i])

stack1.call_is_empty()

print("pop all")
while True:
    if stack1.is_empty():
        break
    else:
        print(stack1.pop())

stack1.call_is_empty()

print("release stack")
del stack1
del sto1

print("Page 117 / 3")


class RoundQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        return False

    def line_up(self, elem):
        self.queue += [elem]

    def get_job(self):
        elem = self.queue[0]
        del self.queue[0]
        return elem

    def index(self, index):
        return self.queue[index % len(self.queue)]


print("init")
queue1 = RoundQueue()

print("check if queue is empty")
print(queue1.is_empty())

print("line up a, b, c")
sto1 = {"a": 1, "b": 1, "c": 4}
for i in sto1:
    queue1.line_up(sto1[i])

print("get a job in queue")
print(queue1.get_job())

print("line up d, e, f")
sto1 = {"d": 5, "e": 1, "f": 4}
for i in sto1:
    queue1.line_up(sto1[i])

print("get all job")
while True:
    if queue1.is_empty():
        break
    else:
        print(queue1.get_job())


print("release the queue")
del queue1
del sto1
