class Node:
 
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
 

class LinkedList:

    def __init__(self):
        self.head = None
 
 
def Circular(head):
    if head == None:
        return True
 
    
    node = head.next
    i = 0
 
    while((node is not None) and (node is not head)):
        i = i + 1
        node = node.next
 
    return(node == head)
 
if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
 
    llist.head.next = second
    second.next = third
    third.next = fourth
 
    if (Circular(llist.head)):
        print('Yes')
    else:
        print('No')
 
    fourth.next = llist.head
 
    if (Circular(llist.head)):
        print('Yes')
    else:
        print('No')