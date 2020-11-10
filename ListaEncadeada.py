#!/usr/bin/env python
# coding: utf-8

# In[7]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
    
class ListaEncadeada:
    print ("Para resultado ordenado: Insira apenas valores inteiros, usando a função lista.insert().") 
    
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0
        
    def insert (self, elem):
        
        if self._size == 0 or elem >= self.last.data:
            return self.insertlast(elem)
        elif elem <= self.first.data:
            return self.insertfirst(elem)
        else: 
            node = Node(elem)
            pointer = self.first
            while pointer.data < node.data:
                pointer = pointer.next
            
            node.next = pointer
            node.previous = pointer.previous
            pointer.previous.next = node
            pointer.previous = node
            self._size = self._size + 1    
        
    def insertfirst (self, elem):
        node = Node(elem)
        node.next = self.first
        node.previous = self.last
        self.first = node
        
        if self._size == 0:
            self.last = node
        else:
            self.first.next.previous = node
            self.last.next = node
        
        self._size = self._size + 1 
        
    def insertlast (self, elem):
        node = Node(elem)
        node.next = self.first
        node.previous = self.last
        self.last = node
        
        if self._size == 0:
            self.first = node
        else:
            self.last.previous.next = node
            self.first.previous = node
        
        self._size = self._size + 1  
         
    
    def removefirst (self):
        if self._size != 0:
           elem = self.first.data
           self.first = self.first.next
           self.first.previous = self.last
           self.last.next = self.first
           self._size = self._size - 1
           return(elem)
        else:
            raise IndexError("A Fila está vazia agora.")
            
    def removelast (self):
        if self._size != 0:
           elem = self.last.data
           self.last = self.last.previous
           self.first.previous = self.last
           self.last.next = self.first
           self._size = self._size - 1
           return(elem)
        else:
            raise IndexError("A Fila está vazia agora.")
        
        
    def peek (self):
        if self._size != 0:
           return (self.first.data) 
        else: 
             raise IndexError("A Fila está vazia agora.")
                
    def restart (self):
        while self.first:
            lista.removelast()
        
        return self._repr_()
        
    def __len__(self):
        return self._size
        
    def __repr__(self):
        
        if self._size > 0:
            r = "" + str(self.first.data)+ " "
            if self._size > 1:
                pointer = self.first.next
                while (pointer!=self.first):
                    r = r + str(pointer.data) + " "
                    pointer = pointer.next
                    
            return r
        return "Fila Vazia..."
        
    def __str__(self):
        return self.__repr__()
    
    def remove(self, index):
        
        if self._size > 0 and index < self._size:
            pointer = self.first
            i = 0
    
            while i != index:
                pointer = pointer.next
                i += 1 
                
            elem = pointer.data    
            
            if index == 0:
                if self._size == 1:
                    self.first = None
                    self.last = None
                    self._size = self._size - 1
                    return(elem)
                
                self.first = self.first.next
                
            if index == self._size - 1:
                self.last = self.last.previous
                
            pointer.next.previous = pointer.previous
            pointer.previous.next = pointer.next
            self._size = self._size - 1
            return (elem)
                
        return "Não será possível..."    
        


# In[38]:


lista = ListaEncadeada()


# In[40]:


len(lista)


# In[41]:


lista


# In[42]:


lista.insertfirst("Paulo")
lista.insertfirst("Ana")
lista.insertlast("Maria")
lista.insertlast("Gabriela")
lista.insertfirst("Pedro")
lista.insertlast("Renata")
lista.insertfirst("João")
lista.insertlast("Sergio")
lista.insertfirst("Ricardo")
lista.insertlast("Bruno")
lista.insertfirst("Angela")


# In[43]:


lista


# In[44]:


lista.removefirst()


# In[45]:


lista.removelast()


# In[46]:


lista.remove(4)


# In[47]:


lista


# In[ ]:




