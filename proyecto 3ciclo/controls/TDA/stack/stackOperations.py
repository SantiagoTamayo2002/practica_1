from controls.TDA.linked.linkedList import Linked_List
from controls.TDA.linked.node import Node

class StackOperations(Linked_List):
    def __init__(self, tope):
        super().__init__()
        self.__head = tope



#                               GETTERS Y SETTERS
#///////////////////////////////////////////////////////////////////////
    @property
    def _head(self):
        print(self.__head)
        return self.__head

    @_head.setter
    def _head(self, value):
        self.__head = value
    
    @property
    def verifyTop(self):
        return self._length < self.__head
    
    @property
    def pop(self):
        if self.isEmpty:
            print("List is Empty")
            return None
        else:
            print("esta entrando?")
            top_element = self.get(0)
            print(self._head)
            self.delete(0)
            return top_element

#///////////////////////////////////////////////////////////////////////

    
    def push(self, data):
        if self.verifyTop:
            self.__addFirst__(data)
        else:
            print("Stack is full")

    