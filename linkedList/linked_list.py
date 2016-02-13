"""linkedList module. Contains classes Node and LinkedList"""

class Node:
    """A very simple Node class

    Instance Variables
        data : contains the object contained within the Node. Each Node can store any object.
        next_node : used to point to the next Node
    """

    def __init__(self, data=None, next_node=None):
        """__init__ initializes each Node instance

        Sets data: to object passed in or None
        Sets next_node: to None
        """
        self.data = data
        self.next_node = next_node

class LinkedList:
    """A typical LinkedList class

    Functions:
        __init__(self, head=None)
        add_head(self, new_node)
        add_tail(self, new_node)
        remove_head(self)
        remove_tail(self)
        get_size(self)
        print(self)
    Instance Variables:
        head: pointer to head of the linked list
        tail: pointer to tail of the linked list
        size: current size of the linked list 
    """

    def __init__(self, head=None):
        """__init__ initializes each LinkedList instance

        sets head to None or to the Node passed in
        """
        self.size = 0
        if head != None:
            self.head = head
            self.tail = head
            self.size = 1

    def add_head(self, new_node):
        """add_head adds new_node to head of our linked list instance"""
        if self.size == 0:
            self.head, self.tail = new_node, new_node
        elif self.size == 1:
            self.head.next_node = new_node
            self.head = self.tail
            self.tail = self.head.next_node
        else:
            new_node.next_node, self.head = self.head, new_node
        self.size += 1

    def add_tail(self, new_node):
        """add_tail adds new_node to the tail of our linked list instance"""
        if self.head == None:
            self.add_head(new_node)
        else:
            self.tail.next_node = new_node
            self.tail = new_node
            self.size += 1

    def remove_head(self):
        """removes the current head of the linked list"""
        if self.head == None:
            return
        elif self.head == self.tail:
            self.head, self.tail = None, None
            self.size = 0
        else:
            self.head = self.head.next_node
            self.size -= 1

    def remove_tail(self):
        """removes the current tail of the linked list"""
        if self.tail == None:
            return
        elif self.size == 1:
            self.tail, self.head = None, None
            self.size = 0
        else:
            self.tail = self.head
            # range is inclusive of end point so must be size -2 
            for num in range(0, (self.size - 1)):
                print("Num ", num)
                self.tail = self.tail.next_node
            self.size -= 1
            self.tail.next_node = None
            
    def get_size(self):
        """get_size returns the current number of elements in the linked list"""
        return self.size

    def print(self):
        """prints each data object from head to tail in the linked list"""
        temp = self.head
        for x in range(0, self.size):
            print("data[", x, "] = ", temp.data)
            temp = temp.next_node  
