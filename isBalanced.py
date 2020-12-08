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
 #================================================================================================================   
class Pilha:
    def __init__(self):
        self.top = None
        self._size = 0
    def push (self, node):
        node.next = self.top
        self.top = node
        self._size = self._size + 1
    def pop  (self):
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return node
        raise IndexError("A Pilha está vazia")
    def peek (self):
        if self._size > 0:
            return self.top
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
    
# ==================================================================================
# ====================================================================================
# ===================================================================================   
    
    
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None
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
        
    def minimo(self, node=ROOT):
        if node == ROOT:
            node = self.raiz
        while node.left:
            node = node.left
        return node.data
    
    def maximo(self, node=ROOT):
        if node == ROOT:
            node = self.raiz
        while node.right:
            node = node.right
        return node.data 
    
    def remove(self, valor, node=ROOT):
        if node == ROOT:
            node = self.raiz
        if node == None:
            return node
        if valor < node.data:
            node.left = self.remove(valor, node.left)
        elif valor > node.data:
            node.right = self.remove(valor, node.right) 
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                substituto = self.min(node.right)
                node.data = substituto
                node.right = self.remove(substituto, node.right)
         
        return node
    
    
    
def inorder(raiz):
        no = raiz
        pilha = Pilha()
        while True:
            if no is not None:
                pilha.push(no)
                no = no.left
            elif(pilha):
                no = pilha.pop()
                print(no.data, end=" ")
                
                no = no.right
            else:
                break
        print()   
        
def height(raiz):
    if raiz is None:
        return 0
    return 1 + max(height(raiz.left), height(raiz.right))

def isBalanced(raiz):
    if raiz is None:
        return True
    
    hleft = height(raiz.left)
    hright = height(raiz.right)
    
    l = isBalanced(raiz.left)
    r = isBalanced(raiz.right)
    
    if abs(hleft-hright)<=1:
        return l and r
        
    return False


# In[2]:


arvore = BinariadeBusca()
arvore.insert(120)
arvore.insert(100)
arvore.insert(130)
arvore.insert(80)
arvore.insert(110)
arvore.insert(200)
arvore.insert(150)

arvore1 = BinariadeBusca()
arvore1.insert(42)
arvore1.insert(15)
arvore1.insert(88)
arvore1.insert(6)
arvore1.insert(27)
arvore1.insert(63)
arvore1.insert(94)
arvore1.insert(20)
arvore1.insert(57)
arvore1.insert(71)

arvore2 = BinariadeBusca()
arvore2.insert(42)
arvore2.insert(15)
arvore2.insert(88)
arvore2.insert(6)
arvore2.insert(27)
arvore2.insert(63)
arvore2.insert(94)

arvore3 = BinariadeBusca()
arvore3.insert(42)
arvore3.insert(15)
arvore3.insert(88)
arvore3.insert(27)
arvore3.insert(63)
arvore3.insert(20)
arvore3.insert(57)
arvore3.insert(71)


# In[3]:


arvore.maximo()


# In[4]:


arvore.minimo()


# In[5]:


print(arvore.raiz)


# In[6]:


inorder(arvore.raiz)


# In[7]:


arvore.mostra_largurabst()


# In[8]:


height(arvore.raiz)


# In[9]:


isBalanced(arvore.raiz)


# In[10]:


height(arvore.raiz.left)


# In[11]:


height(arvore.raiz.right)


# In[12]:


inorder(arvore1.raiz)


# In[13]:


arvore1.mostra_largurabst()


# In[14]:


isBalanced(arvore1.raiz)


# In[15]:


isBalanced(arvore2.raiz)


# In[16]:


isBalanced(arvore3.raiz)


# In[ ]:




