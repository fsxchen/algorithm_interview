"""
约瑟夫圆环问题
Desc：
0,1,···,n-1这n个数字排成一个圆圈，
从数字0开始，每次从这个圆圈里删除第m个数字（删除后从下一个数字开始计数）。
求出这个圆圈里剩下的最后一个数字。
"""


# 使用循环链表解决

class Node:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None

class CircularLinkedList:
    def __init__(self) -> None:
        self.size = 0
        self.head = None

    def build_with_list(self, data:list):
        cur = None
        for value in data:
            if self.head == None:
                self.head = Node(data)
                cur = self.head
            cur.next = Node(data)
            cur = cur.next
            self.size += 1
        cur.next = self.head

    def delete(self, node:Node, pre:None):
        if self.size < 1:
            raise "Error"
        self.size -= 1
        pre.next = node.next
    
    def print(self):
        if self.head == None:
            print("===")
            return
        cur = self.head
        while self.head != self.head.next:
            print(cur.value)
            cur = cur.next

def josephus1(n, m):
    if n == 1:
        return
    if m == 1:
        return
    cl = CircularLinkedList()
    cl.build_with_list(range(n))
    cur = cl.head
    index = 0
    while cl.size > 1:
        if index == m - 2:
            cur.next = cur.next.next
            index = 0
            cl.size -= 1
        else:
            index += 1
        cur = cur.next
    cl.print()
            

if __name__ == "__main__":
    j = josephus1(2, 2)
    
        
        

    