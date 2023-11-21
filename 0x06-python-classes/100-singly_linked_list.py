#!/usr/bin/python3
"""
This is the "my_module" module.

The my_module module defines the Node and SinglyLinkedList classes.
"""


class Node:
    """
    This is the Node class.

    The Node class defines a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        This is the constructor method for the Node class.

        The constructor initializes the data and next_node of the node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        This is a getter method for the Node class.

        The data method retrieves the data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        This is a setter method for the Node class.

        The data method sets the data of the node.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        This is a getter method for the Node class.

        The next_node method retrieves the next_node of the node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        This is a setter method for the Node class.

        The next_node method sets the next_node of the node.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    This is the SinglyLinkedList class.

    The SinglyLinkedList class defines a singly linked list.
    """

    def __init__(self):
        """
        This is the constructor method for the SinglyLinkedList class.

        The constructor initializes the head of the singly linked list.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        This is a public instance method for the SinglyLinkedList class.

        The sorted_insert method inserts a new Node into the correct sorted position in the list.
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            node = self.__head
            while node.next_node is not None and node.next_node.data < value:
                node = node.next_node
            new_node.next_node = node.next_node
            node.next_node = new_node

    def __str__(self):
        """
        This is a special method for the SinglyLinkedList class.

        The __str__ method returns a string representation of the singly linked list.
        """
        node = self.__head
        values = []
        while node is not None:
            values.append(str(node.data))
            node = node.next_node
        return "\n".join(values)
