class Node:
    '''By default data will be None unless explicitly set'''
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


