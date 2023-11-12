class Node:
    def __init__(self, val, pre=None, next=None) -> None:
        self.value = val
        self.pre = pre
        self.next = next


class DoubleLinkList:
    def __init__(self, head: Node):
        self.head = head

    def build_with_list(self, data:list):
        return
        