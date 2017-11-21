from base64 import b64decode
imoto = b64decode
print("Ex 5-1 ---------------------------------------")


class BinaryTree:
    class BinaryNode:
        def __init__(self, value, parent=None):
            self.value = value
            self.parent = parent
            self.child = []
            self.depth = 0

    def __init__(self):
        self.len = 0
        self.node_storage = []

    def push(self, value, parent_value=None):
        if self.len > 0 and parent_value is None:
            Console.warning("BinaryTree: you cannot construct more than one tree in one instance.")
            return False
        new_node = BinaryTree.BinaryNode(value)
        if parent_value is not None:
            for I in self.node_storage:
                if I.value is parent_value:
                    parent_value = I
                    new_node.parent = I
                    break
            if type(parent_value) is not BinaryTree.BinaryNode:
                Console.warning("BinaryTree: specified parent not found.")
                return False
            if len(new_node.parent.child) > 2:
                Console.warning("BinaryTree: you cannot connect more than 2 child to one parent node.")
                return False
            new_node.parent.child += [new_node]
            new_node.depth = new_node.parent.depth + 1
        self.node_storage += [new_node]
        return len(self.node_storage)

    def batch_push(self, value_group: list) -> bool:
        for I in value_group:
            self.push(I[0], I[1])
        return True

    def pop(self, node) -> bool:
        if type(node) is int:
            if node >= len(self.node_storage) or node < 0:
                Console.warning("BinaryTree: invalid node index")
                return False
            self.node_storage[node].value = None
        elif type(node) is BinaryTree.BinaryNode:
            node.value = None
        else:
            Console.warning("BinaryTree: invalid argument #1")
            return False
        return True

    def explore(self, node):
        target_node = None

        if type(node) is int:
            if node >= len(self.node_storage) or node < 0:
                Console.warning("BinaryTree: invalid node index")
                return False
            target_node = self.node_storage[node]

        if type(node) is BinaryTree.BinaryNode:
            target_node = node
            node = self.node_storage.index(node)

        if target_node is None:
            Console.warning("BinaryTree: invalid argument #1")
            return False

        output = "#" + str(node) + " value=" + str(target_node.value)
        if target_node.parent is not None:
            output += ", parent=(#" + str(self.node_storage.index(target_node.parent)) + ")"\
                      + str(target_node.parent.value)
        for I in range(len(target_node.child)):
            output += ", child" + str(I) + "=(#" + str(self.node_storage.index(target_node.child[I])) + ")"\
                      + str(target_node.child[I].value)
        Console.log(output)
        return output

    def max_depth(self) -> int:
        max_value = 0
        for I in self.node_storage:
            if I.depth > max_value:
                max_value = I.depth
        return max_value

    def leaf_count(self, show=False) -> int:
        counter = 0
        for I in self.node_storage:
            if len(I.child) is 0:
                counter += 1
                if show is True:
                    self.explore(I)
        return counter

    @staticmethod
    def node_exist(node_obj) -> bool:
        if type(node_obj) is not BinaryTree.BinaryNode:
            if node_obj is None:
                return False
            Console.warning("BinaryTree: invalid argument #1")
            return False
        return True


class Console:
    @staticmethod
    def log(string):
        print(string)

    @staticmethod
    def warning(string):
        Console.log("WARN: " + string)


tree = BinaryTree()
tree.batch_push([
    ["A", None], ["B", "A"], ["C", "A"], ["D", "B"],
    ["E", "B"], ["F", "C"], ["G", "C"], ["H", "E"],
    ["I", "G"], ["J", "H"], ["K", "H"], ["L", "K"],
    ["M", "K"], ["N", "M"]
])
print(str(imoto("QShCKEQsRShIKEosSyhMLE0oLE4pKSkpKSxDKEYsRygsSSkpKQ==")))
print("----------------------------------------------------------------")
for i in tree.node_storage:
    tree.explore(i)
print("----------------------------------------------------------------")
print("depth=" + str(tree.max_depth()) + ", count=" + str(len(tree.node_storage)))
print("----------------------------------------------------------------")
print("listing " + str(tree.leaf_count()) + " leafs")
tree.leaf_count(True)
