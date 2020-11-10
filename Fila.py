#!/usr/bin/env python
# coding: utf-8

# In[14]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Fila:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0
        
    def push (self, elem):
        node = Node(elem)
        if self._size > 0:
            self.last.next = node
        else:    
            self.first = node
            
        self.last = node    
        self._size = self._size + 1    
        
    def pop (self):
        if self._size != 0:
           elem = self.first.data
           self.first = self.first.next
           self._size = self._size - 1
           return(elem)
        else:
            raise IndexError("A Fila está vazia, mano.")
        
        
    def peek (self):
        if self._size != 0:
           return (self.first.data) 
        else: 
             raise IndexError("A Fila está vazia, mano.")
        
    def __len__(self):
        return self._size
        
    def __repr__(self):
        
        if self._size > 0:
            r = ""
            pointer = self.first
            while (pointer):
                r = r + str(pointer.data) + " "
                pointer = pointer.next
            return r
        return "Fila Vazia..."
        
    def __str__(self):
        return self.__repr__()
    
    
    


# In[15]:


fila = Fila()


# In[16]:


fila


# In[17]:


print(fila)


# In[18]:


fila.push(3)


# In[19]:


fila.push("Fila pronta tuts tuts")


# In[20]:


fila.push(False)


# In[21]:


fila.push(1.2)


# In[22]:


fila.push("Mais um, Mais um")


# In[23]:


fila


# In[24]:


fila.pop()


# In[25]:


fila.peek()


# In[26]:


fila


# In[27]:


fila.pop()


# In[28]:


fila.pop()


# In[29]:


print(fila)


# In[30]:


fila.__len__()


# In[31]:


fila.pop()


# In[32]:


len(fila)


# In[33]:


fila.pop()


# In[34]:


len(fila)


# In[35]:


fila.pop()


# In[36]:


fila.peek()


# In[ ]:




