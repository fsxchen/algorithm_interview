from link_list import SingleLinkList, Node


def reserve_single_link_list(link_list: SingleLinkList):
    if link_list.head == None:
        return
    pre = None
    cur = link_list.head
    while cur:
        next_node = cur.next
        cur.next = pre
        
        pre = cur
        cur = next_node


if __name__ == "__main__":
    s = SingleLinkList()
