# coding = utf-8
'''
给定一个单链表中的一个等待被删除的节点(非表头或表尾)。请在在O(1)时间复杂度删除该链表节点。（脑洞开大点）
给定 1->2->3->4，和节点 3，删除 3 之后，链表应该变为 1->2->4
'''
class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def traverse(head):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    return "->".join(vals)

def deleteNodeO1(node):
    if node.next == None:
        node = None
    else:
        e = node.next
        node.val = e.val
        node.next = e.next

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n1.next = n2
n2.next = n3
n3.next = n4
head = n1
print(traverse(head))
deleteNodeO1(n3)
print(traverse(head))
