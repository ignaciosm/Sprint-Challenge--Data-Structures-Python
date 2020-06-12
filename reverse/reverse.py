class Node:
    def __init__(self, value=None, next_node=None):
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

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # check if list is empty
        if node is None:
            return
        # check if node is last by calling get_next(), if None means it's last node
        if node.get_next() is None:
            # assign node (current last) as head
            self.head = node
            # assign node's prev as the new next
            self.head.set_next(prev)
            return
        # recursively call reverse list
        self.reverse_list(node.get_next(), node)
        # print(node.get_value())
        # if we are in the middle of the list then the next node is the previous one
        node.next_node = prev


list = LinkedList()
print('head:', list.head)

print('~~> add 1')
list.add_to_head(1)
print('head:', list.head.value)
print('next:', list.head.get_next())
print('[1]')

print('~~> add 2')
list.add_to_head(2)
print('head:', list.head.value)
print('next:', list.head.get_next().get_value())
print('[2,1]')

print('~~> add 3')
list.add_to_head(3)
print('head:', list.head.value)
print('next:', list.head.get_next().get_value())
print('[3,2,1]')

print('~~> reverse list')
list.reverse_list(list.head, None)
print('head:', list.head.value)
print('next:', list.head.get_next().get_value())
print('[1,2,3]')