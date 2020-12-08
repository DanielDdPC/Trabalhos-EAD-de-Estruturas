#!/usr/bin/env python
# coding: utf-8

# In[8]:


ROOT = "root"
class Fila:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0
        
    def push (self, elem):
        if self._size > 0:
            self.last.next = elem
        else:    
            self.first = elem
            
        self.last = elem
        self._size = self._size + 1    
        
    def pop (self):
        if self._size != 0:
            elem = self.first
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
    
    
# ========================================================================================================
# ========================================================================================================
# ========================================================================================================
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.next = None
    
    def __str__(self):
         return str(self.data)
        
    
class ArvoreBinaria:
    
    def __init__(self, data=None):
        node = Node(data)
        self.raiz = node
   
    def root(self, node):
        self.raiz = node
        contador =+ 1
    
    def insertleft(self, node, node_pai):
        node_pai.left = node
        contador =+ 1
        
    def insertright(self, node, node_pai):
        node_pai.right = node
        contador =+ 1
        
    def mostra_largura(self, node=ROOT):
        if node == ROOT:
            node = self.raiz
        teste = Fila()
        teste.push(node)
        while len(teste):
            node = teste.pop()
            if node.left:
                teste.push(node.left)
            if node.right:
                teste.push(node.right)
            print(node, end= " ") 
    
    def invert(self, node=None):
        if node is None:
            node = self.raiz
        if node.left and node.right:    
            aux = node.left
            node.left = node.right
            node.right = aux
            self.invert(node.left)
            self.invert(node.right)
        
def full(raiz): 
     
        if raiz is None:     
            return True
      
        if raiz.left is None and raiz.right is None: 
            return True
  
        if raiz.left is not None and raiz.right is not None: 
            return (full(raiz.left) and full(raiz.right)) 
      
        return False   

def height(raiz):
    if raiz is None:
        return 0
    return 1 + max(height(raiz.left), height(raiz.right))
        
tree = ArvoreBinaria()        
        
raiz = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node10 = Node(10)
node11 = Node(11)
node12 = Node(12)
node13 = Node(13)
node14 = Node(14)
node15 = Node(15)

tree.root(raiz)
tree.insertleft(node2, raiz)
tree.insertright(node3, raiz)
tree.insertleft(node4, node2)
tree.insertright(node5, node2)
tree.insertleft(node6, node3)
tree.insertright(node7, node3)
tree.insertleft(node8, node4)
tree.insertright(node9, node5)
tree.insertleft(node10, node6)
tree.insertright(node11, node6)
tree.insertright(node12, node7)
tree.insertleft(node13, node7)
tree.insertright(node14, node4)
tree.insertleft(node15, node5)


# In[9]:


tree.mostra_largura()   


# In[10]:


full(raiz)


# In[11]:


tree.invert()


# In[12]:


tree.mostra_largura()


# In[13]:


tree.invert()


# In[14]:


tree.mostra_largura()


# In[15]:


height(raiz)


# In[ ]:




