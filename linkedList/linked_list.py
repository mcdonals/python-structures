class LinkedList:
    def __init__(self, head=None):
        self.head = head
    def add_head(self, new_node):
        # add error checking
        #   new_node should be a Node and not None
        new_node.next_node, self.head = self.head, new_node
