class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        """Добавить элемент в стэк"""
        new_top = Node(data, self.top)
        self.top = new_top

    def pop(self):
        """Удалить элемент из стека и вернуть значение этого элемента"""
        if self.top is None:
            return None

        deleted = self.top.data
        self.top = self.top.next_node

        return deleted

    def to_list(self):
        """Вернуть данные стека в виде списка"""
        data_list = []

        if self.top is None:
            return data_list

        node = self.top
        while node:
            data_list.append(node.data)
            node = node.next_node

        return data_list


if __name__ == '__main__':
    s = Stack()
    for i in range(1, 10):
        s.push(i)
        print(s.to_list())

    for i in range(1, 12):
        s.pop()
        print(s.to_list())

        #    def test_to_list():
        s = Stack()
        assert s.to_list() == []

        #    def test_push():
        s = Stack()
        s.push('data1')
        s.push({'key': 'value'})
        s.push(1000)

        assert s.to_list() == [1000, {'key': 'value'}, 'data1']

        #    def test_pop_empty():
        s = Stack()
        removed = s.pop()

        assert removed is None

        #    def test_push_pop():
        s = Stack()
        s.push(100)
        removed = s.pop()

        assert removed == 100
        assert s.to_list() == []

        #    def test_push_push_pop():
        s = Stack()
        s.push(100)
        s.push([5])

        assert s.pop() == [5]
        assert s.pop() == 100
        assert s.pop() is None
        assert s.to_list() == []
