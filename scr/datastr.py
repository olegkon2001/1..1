class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class Stack:
    def __init__(self, top=None):
        self.top = top

    @property
    def top(self):
        """"Добавляет данные в стэк."""
        return self.top

    @top.setter
    def top(self, value):
        if  isinstance(value, Node):
            self.top = value
        else:
            self.top = Node(value)




if __name__ == '__main__':
    stack = Stack(Node('data1'))
    current_top = stack.top
    stack.top = Node('data2')
    stack.top.next_node = current_top

    current_top = stack.top
    stack.top = Node('data3')
    stack.top.next_node = current_top


    stack.top.data #data3
    stack.top.next_node.data #data2
    stack.top.next_node.next_node.data #data1

    for i in range(33):
        stack.push(f'data{i}')

    'data3'
    'data2'
    'data1'
