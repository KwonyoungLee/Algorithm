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
    # 1. node 를 두개 잡는다.
    # 2. 한 node 를 다른 node 보다 k 만큼 떨어지게 한다.
    # 3. 그리고 계속 한 칸 씩 같이 이동한다.
    # 4. 만약 더 빠른 노드가 끝에 도달했다면
    #    느린 노드는 끝에서 k 만큼 떨어진 노드가 되므로
    #    바로 반환하자.
    # fast node : O(N)
    # slow node : O(N-K)
    def get_kth_node_from_last(self, k):
        slow = self.head
        fast = self.head

        # fast node 를 k 번째 까지 옮긴다.
        for i in range(k):
            fast = fast.next

        # fast node 값이 None 이 될때까지
        # slow node 를 옮긴다.
        # slow 값은 뒤에서 k 번째 값이 된다.
        while fast is not None:
            fast = fast.next
            slow = slow.next

        return slow


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)