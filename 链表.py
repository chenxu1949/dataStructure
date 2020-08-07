class Node(object):
    def __init__(self,data):
        # 链表的数据域
        self.data = data
        # 链表的引用域
        self.next = None

if __name__ == '__main__':
    node1 = Node(123)
    node2 = Node("abc")
    node3 = Node([1,2,3])
    node4 = Node((1,2,3))

    head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    print(head.data)
    print(head.next.data)
    print(head.next.next.data)
    print(head.next.next.next.data)

