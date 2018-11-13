import random
from math import ceil

class Node:
    def __init__(self, d, next = None):
        self.next = next
        self.data = d


    def __repr__(self):
        return "data: " + str(self.data) + "\nnext: " + str(self.next)


    def delete_node(self, d):
        start_node = self
        n = self
        if n.data == d:
            return n.next    

        while n.next != None:
            n = n.next
            if type(n) is not Node:
                raise TypeError
            if n.next != None:
                if n.next.data == d:
                    if n.next.next != None:
                        n.next = n.next.next
                    else:
                        n.next = None

        return start_node


    def remove_dups(self):
        n = self
        while n.next != None:
            n.next.delete_node(n.data)
            n = n.next

class LinkedList (list):
    def __init__(self, *args):
        x = list(*args)
        for i in x:  # need to learn how to work w/ *args
            self.append(Node(i))



    def append(self, node):  # this will need to be altered if we want it to work generally
        super().append(node)
        if len(self) > 1:
            self[-2].next = self[-1]





if __name__ == '__main__':
    linked_list = LinkedList()
    for i in range(20):
        linked_list.append(Node(ceil(20*random.random())))

    head_node = linked_list[0]
    print(head_node)
    head_node.remove_dups()
    print(head_node)
