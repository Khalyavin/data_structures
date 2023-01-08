class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        """Дабавляет в бинарное дерево поиска новый узел с данными Node(data)"""
        if self.root is None:
            self.root = Node(data)
            print(f'Add {data} to root')
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, node):
        if data['id'] < node.data['id']:
            if node.left is None:
                print(f'Add {data} to left side of {node.data}')
                node.left = Node(data)
            else:
                print(f'Search for {data} place to left side')
                self._insert_recursive(data, node.left)

        elif data['id'] > node.data['id']:
            if node.right is None:
                print(f'Add {data} to right side of {node.data}')
                node.right = Node(data)
            else:
                print(f'Search for {data} place to right side')
                self._insert_recursive(data, node.right)

    def search(self, vacancy_id):
        """
        Возвращает данные о вакансии с полем id, равным vacancy_id.
        Возвращает False, если нет вакансии с id, равным vacancy_id.
        """
        if self.root is None:
            return False
        return self._search_recursive(vacancy_id, self.root)

    def _search_recursive(self, vacancy_id, node):
        if vacancy_id == node.data['id']:
            print(f'Found {vacancy_id}!')
            print(node.data)
            return node.data

        if vacancy_id < node.data['id'] and node.left is not None:
            print(f'search for {vacancy_id} at left side')
            self._search_recursive(vacancy_id, node.left)

        if vacancy_id > node.data['id'] and node.right is not None:
            print(f'search for {vacancy_id} at right side')
            self._search_recursive(vacancy_id, node.right)

        return False


if __name__ == '__main__':
    # bst = BinarySearchTree()
    # bst.insert(40)
    # bst.insert(30)
    # bst.insert(50)
    # bst.insert(20)
    # bst.insert(45)

    bst = BinarySearchTree()
    result = bst.search(1)
    assert result is False


    bst = BinarySearchTree()

    bst.insert({'id': 4, 'company_name': 'name4'})
    bst.insert({'id': 8, 'company_name': 'name8'})
    bst.insert({'id': 2, 'company_name': 'name2'})
    bst.insert({'id': 9, 'company_name': 'name9'})

    assert bst.search(9) == {'id': 9, 'company_name': 'name9'}
    assert bst.search(4) == {'id': 4, 'company_name': 'name4'}
    assert bst.search(1) is False
