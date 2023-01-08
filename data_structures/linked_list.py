class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def to_list(self):
        """Возвращает список, содержащий данные узлов связанного списка"""
        data_list = []
        if self.head is None:
            return data_list

        node = self.head
        while node:
            data_list.append(node.data)
            node = node.next_node

        return data_list

    def print_ll(self):
        """Возвращает строку-представление связанного списка для печати"""
        data_string = ''
        if self.head is None:
            return 'None'

        node = self.head
        while node:
            if data_string == '':
                data_string = str(node.data)
                node = node.next_node
            else:
                data_string = data_string + ' -> ' + str(node.data)
                node = node.next_node

        return data_string + ' -> None'


    def insert_beginning(self, data):
        """Добавить данные в началов связанного списка"""
        if self.head is None:
            self.head = self.tail = Node(data, None)
            return
        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_end(self, data):
        """Добавить данные в конец связанного списка"""
        if self.head is None:
            self.head = self.tail = Node(data, None)
            return
        self.tail.next_node = Node(data, None)
        self.tail = self.tail.next_node

    def get_vacancy_by_id(self, vacancy_id):
        """Получить данные из связанного списка по id"""
        node = self.head
        while node:
#            print(node.data['id'])
            if node.data['id'] == vacancy_id:
                return node.data
            node = node.next_node

        return None


if __name__ == '__main__':
#  def test_print_ll_empty():
    ll = LinkedList()

    assert ll.print_ll() == 'None'


#  def test_print_ll():
    ll = LinkedList()
    node3 = Node(1000, None)
    node2 = Node({'id': 1}, node3)
    node1 = Node('data1', node2)
    ll.head = node1

    assert ll.print_ll() == "data1 -> {'id': 1} -> 1000 -> None"


#  def test_insert_beginning():
    ll = LinkedList()
    ll.insert_beginning('data')

    assert ll.print_ll() == 'data -> None'


#  def test_insert_beginning_twice():
    ll = LinkedList()
    ll.insert_beginning('data2')
    ll.insert_beginning('data1')

    assert ll.print_ll() == 'data1 -> data2 -> None'


#  def test_insert_at_end():
    ll = LinkedList()
    ll.insert_at_end('data1')

    assert ll.print_ll() == 'data1 -> None'


#  def test_insert_at_end_twice():
    ll = LinkedList()
    ll.insert_at_end('data1')
    ll.insert_at_end('data2')

    assert ll.print_ll() == 'data1 -> data2 -> None'


#  def test_insert_at_end_beginning():
    ll = LinkedList()
    ll.insert_at_end('data2')
    ll.insert_beginning('data1')

    assert ll.print_ll() == 'data1 -> data2 -> None'


#  def test_to_list_empty():
    ll = LinkedList()

    assert ll.to_list() == []


#  def test_to_list():
    ll = LinkedList()
    ll.insert_beginning('data2')
    ll.insert_beginning('data1')

    assert ll.to_list() == ['data1', 'data2']


#  def test_get_vacancy_by_id():
    ll = LinkedList()
    ll.insert_beginning({'id': 1, 'key1': 'value1'})
    ll.insert_beginning({'id': 2, 'key2': 'value2'})

    assert ll.get_vacancy_by_id(1) == {'id': 1, 'key1': 'value1'}
    assert ll.get_vacancy_by_id(2) == {'id': 2, 'key2': 'value2'}
    assert ll.get_vacancy_by_id(0) is None


