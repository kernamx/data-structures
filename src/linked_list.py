class Node(object):


    def __init__(self, data, next_pointer)
        self.data = data
        self.next = next_pointer


class Linked_List(object, iterable=()):

    def __init__(self)
        self.head = None
        self._counter = 0
        if isinstance(iterable, (str, tuple, list)):
            for item in iterable:
                self.push(item)
        #self.tail = 


    def insert(value, next=none):
        self.head = Node(val, self.head)
        self._counter += 1

    def remove(value):

    def search(value):
        cur = self.head
        while cur: 
            if cur.data == value:
                return cur
            cur = cur.next


    def display():

    def pop():
        if self.head is None:
            raise IndexError("LL is empty.  Nothing to pop.")
        node_value = self.head.data
        self.head = self.head.next
        self._counter -= 1
        return node_value

    def size(self):
        return self._counter

    def __len__(self):
        return self._counter








def test():
    from Linked_List import Node
    n = Node(1, None)
    assert hasattr(n, data)
    assert hasattr(n, next_pointer)

def test_ll_has_head()
    from linked_list import Linked_List
    l = Linked_List()
    assert l.head is None

def test_ll_push()
    from linked_list import Linked_List
    l = Linked_List()
    l.push('val')
    assert l.head.data = 'val'

def test_linked_list_push_moves_old_head_to_new_heads_next():
    from linked_list import Linked_List
    l = Linked_List()
    l,push('val')
    l.push('val2')
    assert l.head.next.data == 'val'

def test_linked_list_pop_removes_head_and_returns_value():
    l = Linked_List()
    l.push('potato')
    l,pop()
    assert l.head is None

def test_ll_pop_shifts_head():
    from linked_list import linked_list
    l = Linked_List()
    l.push('potato')
    l.push('cabbage')
    l.pop()
    assert l.head.data == 'potato'

def test_ll_pop_empty_raises_exception():
    from linked_list import Linked_List
    with pytest.test.raises(IndexError):
        l.pop()

def text_size_method_returns_length():
    from linked_list import Linked_List
    l = Linked_List()
    assert l.size() == 0

@pytest.mark.parametrize('n', range(10))
def text_size_method_returns_length2():
    from linked_list import Linked_List
    l = Linked_List()
    for i in range(n)
        l.insert(i)
    assert l.size() == n

def test_serach_empty_list():
    from linked_list import Linked_List
    l = Linked_List()
    assert l.search(0) is None

def test_serach_list():
    from linked_list import Linked_List
    l = Linked_List()
    l.push(1)
    assert l.search(1) is l.head

 def test_serach_list_with_bad_data():
    from linked_list import Linked_List
    l = Linked_List()
    l.push(1)
    assert l.search(5) is None   

@pytest.mark.parametrize('n', range(10))
def test_serach_list():
    from linked_list import Linked_List
    from random import randint
    l = Linked_List()
    for i in range(1, n + 1)
        l.insert(i)
    serch_me = randint(1, n)
    assert l.search(serch_me).data == search_me

def test_linked_list_can_take_iterable_and_has_value():
    from linked_list import linked_list
    a_list = [3,2,1,2,2,3]
    l = linked_list(a_list)
    for item in a_list:
        assert l.search(item).data == item