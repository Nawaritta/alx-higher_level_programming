#!/usr/bin/python3

"""Python classes"""


class Node:
    """Class Node"""

    def __init__(self, data, next_node=None):
        """Constructor of the class Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter of data."""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Setter for dataa"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for next_node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Setter for next_node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class Singlylinkedlist"""

    def __init__(self):
        """Constractor of SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.

        The node is inserted respectiong the increasing order of the data.

        Args:
            value (Node): The new Node to insert.
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """Returns a string representation of the linked list"""
        nodes = []
        tmp = self.__head
        while tmp is not None:
            nodes.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(nodes))
