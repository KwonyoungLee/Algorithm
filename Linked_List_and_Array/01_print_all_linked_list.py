# linked_list 구현

# 데이터를 저장할 칸을 만들기.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        # 만약 아무 데이터도 없다면 (head 가 None 이라면)
        if self.head is None:
            self.head = Node(data)
            return

        # next 가 None 일때까지 옮겨간다
        cur = self.head
        while cur.next is not None:
            cur = cur.next

        # 다음 노드로 지정해준다
        cur.next = Node(data)

    # 모든 원소들을 차례대로 프린트
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


# [3] -> [4] -> [5] -> [6]
linked_list = LinkedList(3)

linked_list.append(4)
linked_list.append(5)
linked_list.append(6)

linked_list.print_all()

