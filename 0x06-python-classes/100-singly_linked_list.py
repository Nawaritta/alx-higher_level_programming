#!/usr/bin/python3

"""Python Classes"""


class Node:
    """Class Nodes."""

    def __init__(self, data, next_node=None):
        """Node constructor

        Args:
            data (int): integer
            next_node (Node): The next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter of the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Setter of the data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter of the next_node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Setter of the next node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be None or a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class of a singly-linked list."""

    def __init__(self):
        """Constructor of the SinglyLinkedList class."""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList respecting

                the increasing order of te data nodes values
        Args:
            value (Node): The new Node to insert.
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            tmp = self.head
            while tmp.next_node is not None and value >= tmp.next_node.data:
                tmp = tmp.next_node
                new_node.next_node = tmp.next_node
                tmp.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        """
        nodes = []
        tmp = self.head
        while tmp:
            nodes.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(nodes))
