#!/usr/bin/env python
# coding: utf-8

# In[17]:


class Node(object): 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
        self.height = 1

class BinariadeBusca(object): 
  
    def insert(self, raiz, valor): 
      
        if not raiz: 
            return Node(valor) 
        elif valor < raiz.data: 
            raiz.left = self.insert(raiz.left, valor) 
        else: 
            raiz.right = self.insert(raiz.right, valor) 
  
        raiz.height = 1 + max(self.getHeight(raiz.left), 
                           self.getHeight(raiz.right)) 
  
        balance = self.fator(raiz) 
  
        if balance > 1 and valor < raiz.left.data: 
            return self.rightRotate(raiz) 
  
        if balance < -1 and valor > raiz.right.data: 
            return self.leftRotate(raiz) 
  
        if balance > 1 and valor > raiz.left.data: 
            raiz.left = self.leftRotate(raiz.left) 
            return self.rightRotate(raiz) 
  
        if balance < -1 and valor < raiz.right.data: 
            raiz.right = self.rightRotate(raiz.right) 
            return self.leftRotate(raiz) 
  
        return raiz 
  
    def delete(self, raiz, valor):

        if not raiz:
            return raiz

        elif valor < raiz.data:
            raiz.left = self.delete(raiz.left, valor)

        elif valor > raiz.data:
            raiz.right = self.delete(raiz.right, valor)

        else:
            if raiz.left is None:
                temp = raiz.right
                raiz = None
                return temp

            elif raiz.right is None:
                temp = raiz.left
                raiz = None
                return temp

            temp = self.menorNode(raiz.right)
            raiz.data = temp.data
            raiz.right = self.delete(raiz.right, temp.data)

        if raiz is None:
            return raiz

        raiz.height = 1 + max(self.getHeight(raiz.left), self.getHeight(raiz.right))

        balanco = self.fator(raiz)

        if balanco > 1 and self.fator(raiz.left) >= 0:
            return self.rightRotate(raiz)

        if balanco < -1 and self.fator(raiz.right) <= 0:
            return self.leftRotate(raiz)

        if balanco > 1 and self.fator(raiz.left) < 0:
            raiz.left = self.leftRotate(raiz.left)
            return self.rightRotate(raiz)

        if balanco < -1 and self.fator(raiz.right) > 0:
            raiz.right = self.rightRotate(raiz.right)
            return self.leftRotate(raiz)

        return raiz

    def leftRotate(self, z): 
  
        y = z.right 
        T2 = y.left 
  
        y.left = z 
        z.right = T2 
  
        z.height = 1 + max(self.getHeight(z.left), 
                         self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                         self.getHeight(y.right)) 
  
        return y 
  
    def rightRotate(self, z): 
  
        y = z.left 
        T3 = y.right 
  
        y.right = z 
        z.left = T3 
  
        z.height = 1 + max(self.getHeight(z.left), 
                        self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                        self.getHeight(y.right)) 
  
        return y 
  
    def getHeight(self, raiz): 
        if not raiz: 
            return 0
  
        return raiz.height 
  
    def fator(self, raiz): 
        if not raiz: 
            return 0
  
        return self.getHeight(raiz.left) - self.getHeight(raiz.right) 
    
    def menorNode(self, raiz):
        if raiz is None or raiz.left is None:
            return raiz

        return self.menorNode(raiz.left)
    
    def preOrder(self, raiz): 
  
        if not raiz: 
            return
  
        print("{0} ".format(raiz.data), end="") 
        self.preOrder(raiz.left) 
        self.preOrder(raiz.right) 
  
  
arvore = BinariadeBusca() 
raiz = None
  
raiz = arvore.insert(raiz, 42) 
raiz = arvore.insert(raiz, 15) 
raiz = arvore.insert(raiz, 88) 
raiz = arvore.insert(raiz, 27) 
raiz = arvore.insert(raiz, 63) 
raiz = arvore.insert(raiz, 20)
raiz = arvore.insert(raiz, 57)
raiz = arvore.insert(raiz, 71)



    
# Preorder Traversal 
print("Preorder traversal of the", 
      "constructed AVL tree is") 
arvore.preOrder(raiz) 
print() 

raiz = arvore.delete(raiz, 57)

# Preorder Traversal 
print("Preorder traversal of the", 
      "constructed AVL tree is") 
arvore.preOrder(raiz) 
print() 


# In[18]:


raiz = arvore.delete(raiz, 20)
raiz = arvore.delete(raiz, 42)


# In[19]:


print("Preorder traversal of the", 
      "constructed AVL tree is") 
arvore.preOrder(raiz) 
print() 


# In[20]:


raiz = arvore.insert(raiz, 42) 


# In[21]:


print("Preorder traversal of the", 
      "constructed AVL tree is") 
arvore.preOrder(raiz) 
print() 


# In[ ]:




