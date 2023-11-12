
class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

class SingleLinkList:
    def __init__(self, head=None) -> None:
        self.head = head

    # insert a element in the front
    def insert(self, x) -> None:
        nex = self.head
        x.next = nex
        self.head = x
        


    def build_with_list(self, data_list:list) -> None:
        cur = self.head
        for data in data_list:
            if self.head == None:
                self.head = Node(data)
                cur = self.head
                continue
            
            cur.next = Node(data)
            cur = cur.next

    def print(self):
        cur = self.head
        while cur:
            print(cur.value, end="->")
            cur = cur.next
        print("|")



if __name__ == "__main__":
    s = SingleLinkList()
    s.build_with_list([1, 2, 3, 3,2,1])
    s.insert(Node(0))
    s.print()