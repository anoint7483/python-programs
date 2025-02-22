# creating a node class to create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# create a linked list class
class LinkedList:
    def __init__(self):
        self.head = None                

# Insertion a the beginning of the linked list
def insertAtBegin(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return
    else:
        new_node.next = self.head
        self.head = new_node

# Insertion at given index of the linked list
def insertAtIndex(self,data,index):
    new_node = Node(data)
    current_node = self.head
    position = 0
    if position==index:
        insertAtBegin(data)
    while(current_node!=None and position+1!=index):
        position = position+1
        current_node = current_node.next
    if current_node!=None:
        new_node.next = current_node.next
        current_node.next = new_node
    else:
        print("Index is not found")    

# Insertion at the end of the linked list
def insertAtEnd(self,data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return
    current_node = self.head
    while current_node.next:
        current_node = current_node.next
    current_node.next = new_node    

# Updating the value of a node of linked list
def updateNode(self,value,index):
    current_node = self.head
    position = 0
    if position==index:
        current_node.data = value
    else:    
        while(current_node!=None and position+1!=index):
            position = position+1 
            current_node = current_node.next
        if current_node!=None:
            current_node.data = value
        else:
            print("Index is not found")        

# Deleting first node from the linked list
def deleteFirstNode(self):
    if self.head == None:
        return
    self.head = self.head.next

# Deleting a node whose index is given
    def DeleteAtindex(self,index):
        if self.head == None:
            return
        current_node = self.head
        position = 0
        if position == index:
            self.deleteFirstNode()
        else:
            while(current_node!=None and position+1!=index):
                position = position+1
                current_node = current_node.next
            if current_node!=None:
                current_node.next = current_node.next.next
            else:
                print("Index is not found")      


# Delete last node from the linked list
def deleteLastNode(self):
    if self.head == None:
        return
    current_node = self.head
    while(current_node.next.next):
        current_node = current_node.next
    current_node.next = None

# To remove the node whoose data is given
def deleteNode(self,data):
    current_node = self.head
    if current_node.data == data:
        self.deleteFirstNode()
        return
    while(current_node!=None and current_node.next.data!=data):
        current_node = current_node.next
    if current_node == None:
        return
    else:
        current_node.next = current_node.next.next  
    
# To print or traverse a linked list
def printLL(self):
    current_node = self.head
    while(current_node):
        print(current_node.data)
        current_node = current_node.next

# To get the length of the given Linked list
def sizeOfLL(self):
    size = 0
    if(self.head):
        current_node = self.head
        while(current_node):
            size = size + 1
            current_node = current_node.next
        return size
    else:
      return 0


# Testing our functions    

# creating a new linked list
llist = LinkedList() 
# adding node to the linked list
llist.insertAtEnd("a")
llist.insertAtEnd("b")
llist.insertAtBegin("c")
llist.insertAtEnd("d")
llist.insertAtIndex("f",2)

# to print the linked list
print("Node data")
llist.printLL()
    

     
                   

    



            


