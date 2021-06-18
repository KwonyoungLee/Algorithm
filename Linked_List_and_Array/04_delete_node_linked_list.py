class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    # index  next node
    #  [1]     [2]      [3]
    #        new node
    #          [1.5]
    # index.next = new_node
    # new_node.next = next_node
    def add_node(self, index, value):
        # new_node = 3
        new_node = Node(value)
        # 맨 앞에 넣을 시
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        # node = 5 (0번째 노드)
        node = self.get_node(index-1)
        # next_node = 12
        next_node = node.next
        # 5의 next_node = 3
        node.next = new_node
        # 3의 next_node = 12
        new_node.next = next_node

    #        index-1  -> next_node next_node
    #  [1]     [2]      [3]
    #        new node
    #          [1.5]
    # index.next = new_node
    # new_node.next = next_node
    def delete_node(self, index):
        # 0번째(head) 를 지우고 싶을때
        if index == 0:
            # 다음 노드를 head 노드로 지정해 주면 된다
            self.head = self.head.next
            return
        node = self.get_node(index - 1)
        node.next = node.next.next

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
linked_list.add_node(1, 3)
linked_list.delete_node(1)
linked_list.print_all()