from _collections_abc import Iterable

class Node:
    counter = 0

    def __init__(self, data=None) -> None:
        self.data = data                                            # list element data
        self.next_node = None                                       # link for next list element
        Node.counter += 1                                           # elements in list counter


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        # self.counter = -1

    def __str__(self) -> str:
        print_data = ''
        last_node = self.head
        for i in range(Node.counter):
            print_data += str(last_node.data) + ' '
            last_node = last_node.next_node
        return '[{}]'.format(print_data.rstrip())

    def __iter__(self):
        return self

    def __next__(self) -> any:
        counter = -1
        while counter < Node.counter - 1:
            counter += 1
            return self.get(node_index=counter)
        raise StopIteration

    def append(self, data) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = new_node

    def get(self, node_index) -> any:
        last_node = self.head
        tmp_index = 0
        while tmp_index <= node_index:
            if tmp_index == node_index:
                try:
                    return last_node.data
                except AttributeError:
                    return None
            tmp_index += 1
            last_node = last_node.next_node

    def remove_data(self, rm_data) -> None:           # Удаление по значению
        Node.counter -= 1
        head_node = self.head
        if head_node is not None:
            if head_node.data == rm_data:
                self.head = head_node.next_node
                return
        while head_node is not None:
            if head_node.data == rm_data:
                break
            last_node = head_node
            head_node = head_node.next_node
        if head_node is None:
            return
        last_node.next_node = head_node.next_node

    def remove(self, rm_index) -> None:                          # Удаление по индексу
        Node.counter -= 1
        head_node = self.head
        tmp_index = 0
        if head_node is not None:
            if tmp_index == rm_index:
                self.head = head_node.next_node
                return
        while tmp_index != rm_index:
            if tmp_index == rm_index:
                break
            last_node = head_node
            head_node = head_node.next_node
            tmp_index += 1
        if head_node is None:
            return
        last_node.next_node = head_node.next_node


my_list = LinkedList()
my_list.append(data=10)
my_list.append(data=20)
my_list.append(data=30)
my_list.append(data=40)
my_list.append(data=50)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(rm_index=1)
print('Новый список:', my_list)

print('\nИтерация')
for line in my_list:
    print(line, end=' ')



