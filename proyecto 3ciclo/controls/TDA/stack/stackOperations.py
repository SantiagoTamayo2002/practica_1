from controls.TDA.linked.linkedList import Linked_List

class StackOperations(Linked_List):
    def __init__(self, tope):
        super().__init__()
        self.__head = tope



#                               GETTERS Y SETTERS
#///////////////////////////////////////////////////////////////////////
    @property
    def _head(self):
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
        else:
            self.delete(0)

#///////////////////////////////////////////////////////////////////////

    
    def push(self, data):
        if self.verifyTop:
            self.__addFirst__(data)
        else:
            print("Stack is full")

    