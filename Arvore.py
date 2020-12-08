#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Implemente o algoritmo mostra_largura na classe Arvore, que deve exibir os nós da árvore através de uma estratégia de busca em largura.


# In[1]:


class Node:
    def __init__(self, data):
        self.data = data
        self.prox = []
        
    def adiciona(self, node):
        self.prox.insert(0,node)
    
    def __str__(self):
        return str(self.data)
        
class Arvore:         
    def __init__(self, node):
        self.raiz = node
    def mostra_largura(self):
        node = self.raiz
        self.pintura(node)
        k = 0
        while k < 3:
            for i in reversed(range(len(node.prox))):
               self.pintura(node.prox[i])
            
            if len(node.prox) > 0:
                node = node.prox[len(node.prox)-1]
            k += 1
        
    def pintura(self, node):
        if node is self.raiz:
            print(node.data)
            
        if node.prox is not None:
            for i in reversed(range(len(node.prox))):    
                print (node.prox[i].data)      
        
        
raiz = Node(1)
arvore = Arvore(raiz)
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

raiz.adiciona(node2)
raiz.adiciona(node3)
raiz.adiciona(node4)
node2.adiciona(node5)
node2.adiciona(node6)
node3.adiciona(node7)
node4.adiciona(node8)
node4.adiciona(node9)
node5.adiciona(node10)
node5.adiciona(node11)

     
    


# In[2]:


arvore.pintura(raiz)


# In[3]:


arvore.mostra_largura()


# In[ ]:




