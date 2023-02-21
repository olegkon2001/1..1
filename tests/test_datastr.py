import unittest
from scr.datastr import Node,Stack





class TestNode(unittest.TestCase):
    """Тест класса Node"""

    def setUp(self) -> None:
        self.node_10 = Node(10)



    def test_node_init1(self):
        assert self.node_10.data == 10
        self.node_10 = Node(100)
        assert self.node_10.next_node is None

    def test_node_init2(self):
        assert self.node_10.data == 10



    def test_node_next_node(self):
        """Проверим, что next_node ссылается на узел."""
        node2 = Node(220, self.node_10)
        assert node2. next_node is self.node_10


class TestStack(unittest.TestCase):
    def test_stack_top(self):
        pass