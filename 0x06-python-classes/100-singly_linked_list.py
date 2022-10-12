#!/usr/bin/python3
"""
    Defines a Singly linked list and its node
"""


class Node:
    """
        A node representation
    """
    def __init__(self, data, next_node=None):
        """
            Instantiates instance attributes
            Args:
                data (int): integer value contained in the node
                next_node(Node or None): next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves data"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """ Sets data value"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves next node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Sets next node"""
        if (value is not None and not isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
        A singly linked list
    """
    def __init__(self):
        """Instantiation"""
        self.__head = None
        tmp = self.__head

    def sorted_insert(self, value):
        new = Node(value)

        if (self.__head is None):
            self.__head = new
            return

        if (new.data < tmp.data):
            new.next_node = tmp
            self.__head = new
            return

        while (tmp.next_node is not None):
            if (tmp.next_node.data < new.data):
                tmp = tmp.next_node
            else:
                new.next_node = tmp.next_node
                tmp.next_node = new
                return

        tmp.next_node = new

    def __str__(self):
        tmp = self.__head
        if tmp is None:
            return ("")
        while (tmp.next_node is not None and tmp):
            print(tmp.data)
            tmp = tmp.next_node
        return (str(tmp.data))
