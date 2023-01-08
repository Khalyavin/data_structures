class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size

    def custom_hash(self, key):
        """Возвращает целое число (хеш-значение), находящееся в пределах от 0 до table_size"""
        hash_value = 0
        for i in key:
            hash_value += ord(i)
            hash_value = (hash_value * ord(i))
        return hash_value % self.table_size

    def add_key_value(self, key, value):
        """
        Добавить новый узел Node(Data(key, value) в хеш-таблицу hash_table[hashed_key]=Node(...)
        При возникновении коллизии строится связанный список.
        """
        hash_key = self.custom_hash(key)
        if self.hash_table[hash_key] is None:
            self.hash_table[hash_key] = Node(Data(key, value), None)
        else:
            node = self.hash_table[hash_key]
            while node.next_node:
                node = node.next_node

            node.next_node = Node(Data(key, value), None)

    def get_value(self, key):
        """Получить значение (атрибут value класса Data) по ключу key"""
        hash_key = self.custom_hash(key)
        if self.hash_table[hash_key] is not None:
            node = self.hash_table[hash_key]
            while node.next_node:
                if key == node.data.key:
                    return node.data.value
                node = node.next_node
            return node.data.value

        return None

    def print_ht(self):
        print('{')
        for i, node in enumerate(self.hash_table):
            if node:
                ll_str = ''
                if node.next_node:
                    while node.next_node:
                        ll_str += str(node.data.key) + ': ' + str(node.data.value) + ' --> '
                        node = node.next_node
                    ll_str += str(node.data.key) + ': ' + str(node.data.value) + ' --> None'
                    print(f'    [{i}]  {ll_str}')
                else:
                    print(f'    [{i}]  {node.data.key}: {node.data.value}')
            else:
                print(f'    [{i}] None')
        print('}')


if __name__ == '__main__':
    ht = HashTable(5)
    ht.add_key_value('key0', 'value0')
    ht.add_key_value('key1', 'value1')
    ht.add_key_value('key2', 'value2')
    ht.add_key_value('key3', 'value3')
    ht.add_key_value('key4', 'value4')
    ht.add_key_value('key5', 'value5')

    ht.print_ht()

    assert ht.custom_hash('key0') == 2
    assert ht.custom_hash('key2') == 0
    assert ht.custom_hash('key5') == 2

    assert ht.get_value('key4') == 'value4'
    assert ht.get_value('key14') == None

    assert ht.hash_table[4] == None


