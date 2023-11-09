from link_list import SingleLinkList, Node


def reserve_single_link_list(link_list: SingleLinkList):
    if link_list.head == None:
        return
    pre = None
    cur = link_list.head
    while cur != None:
        