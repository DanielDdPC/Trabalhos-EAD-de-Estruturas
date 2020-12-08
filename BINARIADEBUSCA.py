#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
    
# ==================================================================================
# ====================================================================================
# ===================================================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.next = None
    
    def __str__(self):
         return str(self.data)
        
        
        
class ArvoreBinaria:
    
    def __init__(self, data=None, node=None):
        if node:
            self.raiz = node
        elif data:    
            node = Node(data)
            self.raiz = node
        else:
            self.raiz = None
   
    def root(self, node):
        self.raiz = node
    
    def insertleft(self, node, node_pai):
        node_pai.left = node

    def insertright(self, node, node_pai):
        node_pai.right = node     
    
    def mostra_largura(self, node=ROOT):
        if node == ROOT:
            node = self.raiz
        fila = Fila()
        fila.push(node)
        while len(fila):
            node = fila.pop()
            if node.left:
                fila.push(node.left)
            if node.right:
                fila.push(node.right)
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

            


# In[2]:


class BinariadeBusca(ArvoreBinaria):
    def insert (self, valor):
        pai = None
        x = self.raiz
        while x:
            pai = x
            if valor < x.data:
                x = x.left
            else:
                x = x.right
        if pai is None:
            self.raiz = Node(valor)
        elif valor < pai.data:
            pai.left = Node(valor)
        else:
            pai.right = Node(valor)
            
    def search (self, valor, node=0):
        if node == 0:
            node = self.raiz
            print ("node == 0")
        if node is None:
            return node
        if node.data == valor:
            return BinariadeBusca(node)
        if valor < node.data:
            return self.search (valor, node.left)
        return self.search (valor, node.right)

    def mostra_largurabst(self, node=ROOT):
        if node == ROOT:
            node = self.raiz
        fila = Fila()
        fila.push(node)
        while len(fila):
            node = fila.pop()
            if node.left:
                fila.push(node.left)
            if node.right:
                fila.push(node.right)
            print(node, end= " ")    


# In[3]:


arv_bst = BinariadeBusca()

arv_bst.insert(200)
arv_bst.insert(100)
arv_bst.insert(80)
arv_bst.insert(150)
arv_bst.insert(120)
arv_bst.insert(110)
arv_bst.insert(130)
arv_bst.insert(300)
arv_bst.insert(250)
arv_bst.insert(270)
arv_bst.insert(277)
arv_bst.insert(273)
arv_bst.insert(275)
arv_bst.insert(220)
arv_bst.insert(260)
arv_bst.insert(265)
arv_bst.insert(400)
arv_bst.insert(500)
arv_bst.insert(350)


# In[4]:


print(arv_bst.raiz)


# In[5]:


arv_bst.mostra_largurabst()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




