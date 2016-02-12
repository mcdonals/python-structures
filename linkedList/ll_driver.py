#!/usr/bin/python3
from node import *
from linked_list import *

# You can create and fill node with any object automatically, yay python!
n = Node(5)

# this is where n is in memory
print('&n = ', id(n))

# Create linked list that adds Node we just created
ll = LinkedList(n)
print('&ll = ', id(ll))
print('&ll.head = ', id(ll.head))
print('ll.head points to n, yay!')

# Create another new node
n = Node(7)
print('Now n is a new node variable')
print('&n = ', id(n))
print('&ll = ', id(ll))
print('&ll.head = ', id(ll.head))
print('ll.head still points to the orignal n, double yay!')

# add to head the new node
ll.add_head(n)

# now walk the linked list to make sure we have two items and no more
print('walking linked list')
temp = ll.head
while temp != None:
    print(temp.data)
    temp = temp.next_node

# and rewalk it just to be sure we didn't butcher our links actual poitners
print('walking again')
temp = ll.head
while temp != None:
    print(temp.data)
    temp = temp.next_node
