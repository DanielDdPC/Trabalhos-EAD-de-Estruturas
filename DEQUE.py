#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
    
class DequeDinamico:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0
        
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
            raise IndexError("A Fila está vazia, mano.")
            
    def removelast (self):
        if self._size != 0:
           elem = self.last.data
           self.last = self.last.previous
           self.first.previous = self.last
           self.last.next = self.first
           self._size = self._size - 1
           return(elem)
        else:
            raise IndexError("A Fila está vazia, mano.")
        
        
    def peek (self):
        if self._size != 0:
           return (self.first.data) 
        else: 
             raise IndexError("A Fila está vazia, mano.")
                
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
    


# In[6]:


lista = DequeDinamico()


# In[7]:


len(lista)


# In[8]:


lista


# In[9]:


lista.insertfirst(2)


# In[10]:


lista


# In[11]:


lista.insertfirst("Daniel")


# In[12]:


lista


# In[13]:


lista.insertlast("Mais uma né")


# In[14]:


lista


# In[15]:


len(lista)


# In[16]:


len(lista)


# In[17]:


len(lista)


# In[18]:


lista.insertlast(6)


# In[19]:


lista


# In[20]:


lista.removelast()


# In[21]:


lista.removefirst()


# In[22]:


lista.removefirst()


# In[23]:


lista.removelast()


# In[24]:


lista.removelast()


# In[25]:


lista.removefirst()


# In[26]:


lista.removefirst()


# In[27]:


lista.removefirst()


# In[28]:


lista.removefirst()


# In[29]:


lista.removelast()


# In[30]:


len(lista)


# In[31]:


lista


# In[32]:


lista.insertfirst(5)


# In[33]:


lista.insertlast(True)


# In[34]:


lista.insertfirst("Tentativa")


# In[35]:


lista


# In[36]:


len(lista)


# In[37]:


lista.restart()


# In[38]:


len(lista)


# In[39]:


lista


# In[40]:


lista.insertfirst(654)


# In[41]:


lista.insertlast(666)


# In[42]:


lista.insertlast("agoravamove")


# In[43]:


lista.removelast()


# In[44]:


lista.removelast()


# In[45]:


lista


# In[46]:


len(lista)


# In[47]:


lista


# In[48]:


lista.restart()


# In[49]:


lista.insertfirst(10)


# In[50]:


lista


# In[51]:


len(lista)


# In[52]:


lista.insertlast(2)


# In[53]:


lista


# In[54]:


lista.removefirst()


# In[55]:


lista


# In[56]:


lista.insertlast(2)


# In[57]:


lista.removelast()


# In[58]:


lista


# In[59]:


lista.removelast()


# In[61]:


lista


# In[62]:


lista.insertlast(2)


# In[63]:


lista


# In[ ]:





# In[ ]:




