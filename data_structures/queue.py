class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """Добавить данные в очередь"""
        if self.tail is None and self.head is None:
            self.head = self.tail = Node(data, None)
            return
        self.tail.next_node = Node(data, None)
        self.tail = self.tail.next_node

    def dequeue(self):
        """Забрать данные из очереди"""
        if self.head is None:
            return None

        deleted = self.head.data
        self.head = self.head.next_node
        if self.head is None:
            self.tail = None

        return deleted

    def to_list(self):
        """Вернуть данные очереди в виде списка"""
        data_list = []

        if self.head is None:
            return data_list

        node = self.head
        while node:
            data_list.append(node.data)
            node = node.next_node

        return data_list


if __name__ == '__main__':
    q = Queue()
    for i in range(1, 11):
        q.enqueue(i)
        print(q.to_list())

    for i in range(1, 12):
        q.dequeue()
        print(q.to_list())


#  def test_queue_to_list():
    q = Queue()

    assert q.to_list() == []


#  def test_queue_enqueue():
    q = Queue()
    q.enqueue('data1')
    q.enqueue('data2')

    assert q.to_list() == ['data1', 'data2']


#  def test_queue_dequeue_empty():
    q = Queue()
    q.dequeue()

    assert q.to_list() == []


#  def test_queue_dequeue():
    q = Queue()
    q.enqueue('data1')
    q.dequeue()

    assert q.to_list() == []


#  def test_queue_dequeue2():
    q = Queue()
    q.enqueue('data1')
    q.enqueue('data2')
    q.dequeue()

    assert q.to_list() == ['data2']

