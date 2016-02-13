#!/usr/bin/python3
from linked_list import *

# Create linked list that adds Node we just created
n = Node(3)
ll = LinkedList(n)

# Create another new node
n = Node(7)
ll.add_head(n)

# Create another new node
n = Node(4)

# add to tail the new node
ll.add_tail(n)
n = Node(4)
ll.add_tail(n)

# now walk the linked list to make sure we have two items and no more
print('walking linked list')
temp = ll.head
while temp != None:
    print(temp.data)
    temp = temp.next_node

print("try print the data the module profides")
ll.print()
