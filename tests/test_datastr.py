import pytest
from scr.datastr import Node,Stack

@pytest.fixture
def node_10():
    return Node(10)



def test_node_init(node_10):
    assert node_10.data == 10
    assert node_10.next_node is None

def test_node_next_node(node_10):
    """Проверим, что next_node ссылается на узел."""
    node2 = Node(220, node_10)
    assert node2.next_node is node_10





