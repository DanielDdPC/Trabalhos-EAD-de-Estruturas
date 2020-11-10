#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None
        
    
class Pilha:

    def __init__(self):
        self.top = None
        self._size = 0
        
    def push (self, elem):
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size = self._size + 1
    
    def pop  (self):
        if self._size > 0:
          node = self.top
          self.top = self.top.next
          self._size = self._size - 1
          return node.data
        raise IndexError("A Pilha está vazia")
    
    def peek (self):
        if self._size > 0:
           return self.top
        raise IndexError("A Pilha está vazia")
    
    def __len__(self):
        return self._size
    
    def __repr__(self):
        r = ""
        pointer = self.top
        while (pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r
    
    def __str__(self):
        return self.__repr__()
                 


# In[4]:


pilha = Pilha()


# In[5]:


len(pilha)


# In[6]:


pilha


# In[7]:


pilha.push(3)


# In[8]:


pilha.push("DANIEEEL")


# In[9]:


pilha.push(True)


# In[10]:


pilha.push("Estou Orgulhoso e Feliz")


# In[11]:


print(pilha)


# In[12]:


len(pilha)


# In[13]:


pilha.pop()


# In[14]:


pilha.pop()


# In[15]:


pilha.push("Ainda estou feliz ok")


# In[16]:


pilha


# In[17]:


pilha


# In[18]:


pilha.push("THREE NIGHT AT THE MOTEL")


# In[19]:


pilha


# In[20]:


pilha.pop()


# In[21]:


pilha


# In[22]:


pilha.pop()


# In[23]:


pilha


# In[24]:


pilha.pop()


# In[25]:


pilha.pop()


# In[ ]:





# In[ ]:




