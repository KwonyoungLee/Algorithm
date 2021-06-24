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

    # head -> next -> next -> next -> None
    # 끝이 언제 인지 -바로- 알 수 없음
    # 전체의 길이를 알아낸 다음 길이에서 k 값을 빼면 가능
    # 1. 전체 길이 알아내기
    # 2. 그 길이에서 k 만큼 뺀 길이만큼 이동
    def get_kth_node_from_last(self, k):
        length = 1
        cur = self.head

        # head 에서 next next 가면서 length 측정
        while cur.next is not None:
            cur = cur.next
            length += 1

        # 총 길이에서 k 번째를 빼면 노드의 위치여부 파악 가능
        end_length = length - k
        cur = self.head

        # 다시 head 부터 end_length 만큼 next 하여 node 값 반환
        for i in range(end_length):
            cur = cur.next
        return cur


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!