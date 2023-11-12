
class SingleLinkedList:
    def __init__(self) -> None:    
        pass
    

def reserve_single_link_list(head: Node):
    if head == None:
        return
    pre = None
    cur = head
    while cur:
        next_node = cur.next
        cur.next = pre
        
        pre = cur
        cur = next_node

    return pre


if __name__ == "__main__":
    s = SingleLinkList()
    s.build_with_list([1, 2, 3])
    s.print()
    new_head = reserve_single_link_list(s.head)
    s.head = new_head
    s.print()
