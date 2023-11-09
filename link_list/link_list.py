
class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

class SingleLinkList:
    def __init__(self, head=None) -> None:
        self.head = head