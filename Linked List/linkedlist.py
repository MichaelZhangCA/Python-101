class Node():
    
    def __init__(self, val, nextNode=None, prevNode=None, mark=''):
        self.value = val
        self.next = nextNode
        self.prev = prevNode
        self.mark = mark

    def addNextNode(self, val):
        to_add = Node(val)
        
        if (self.next):
            to_add.next = self.next
            self.next.prev = to_add
        
        self.next = to_add
        to_add.prev = self
        
        return to_add

    def deleteNextNode(self):
        self.next = self.next.next
        if (self.next.next):
            self.next.next.prev = self
    
    def traverseForewards(self):
        res = []
        node = self
        while (node):
            res.append(node.mark if node.mark else str(node.value))
            node = node.next
            
        print(" -> ".join(res))

    def traverseBackwards(self):
        res = []
        node = self
        while (node):
            res.append(node.mark if node.mark else str(node.value))
            node = node.prev
            
        print(" <- ".join(list(reversed(res))))
    
    def getNextN(self, n):
        node = self
        i = 0
        while (node):
            node = node.next
            i += 1
            if (i==n):
                break
                
        return node
    
    
class LinkedList():
    
    def __init__(self):
        
        self.head = Node(0, mark='H')
        self.tail = Node(0, mark='T')
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def show(self, reverse=False):
        
        if (reverse):
            self.tail.traverseBackwards()
        else:
            self.head.traverseForewards()

    def getAt(self, idx):
        node = self.head.getNextN(idx)
        return None if (node is None or node.mark!="") else node
    
    def insertAt(self, idx, val):
        node = self.head.getNextN(idx)
        if (node):
            return node.addNextNode(val)
    
        return None
    
    def addHead(self, val:int):
        # add behind the sentinel head
        added = self.head.addNextNode(val)
        return added
    
    def addTail(self, val:int):
        # add behind the predecessor sentinel tail
        added = self.tail.prev.addNextNode(val)
        return added
    
    def deleteAt(self, idx):
        node = self.getAt(idx)
        if (node):
            node.prev.deleteNextNode()
    
    # purely return the Linked List, without the sentinel nodes
    def getLL(self):
        purehead = self.head.next
        # cut head and tail sentinel nodes
        self.tail.prev.next = None
        self.head.next.prev = None
        self.head.next = None
        
        return purehead
        
def createLL(arr):
    head = Node(0)
    node = head
    for n in arr:
        node.next = Node(n)
        node = node.next
    
    return head.next

def createDLL(arr):
    ll = LinkedList()
    for n in arr:
        ll.addTail(n)
        
    return ll.getLL()
