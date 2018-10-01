# coding = utf-8
'''
删除链表中的元素
给出链表 1->2->3->3->4->5->3, 和 val = 3, 你需要返回删除3之后的链表：1->2->4->5
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

# 此种做法表尾删不掉，抛弃
'''
def deleteNodeA(head, val):
    if not head:
        return None
    else:
        node = head
        while node:
            if node.val == val:
                if node.next is None:
                    node = None
                    break
                else:
                    p = node.next
                    node.val = p.val
                    node.next = p.next
            else:
                node = node.next
    return head
'''

#最普遍的做法
def deleteNodeB(head, val):
    if not head:
        return None
    else:
        pre, node = None, head
        while node:
            if node.val == val:
                if not pre:
                    head = node.next
                else:
                    pre.next = node.next
            else:
                pre = node
            node = node.next
        return head


n1 = Node(30)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(30)
n6 = Node(60)
n7 = Node(30)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
head = n1
print(traverse(head))
#print(traverse(deleteNodeA(head, 30)))
print(traverse(deleteNodeB(head, 30)))