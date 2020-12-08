#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None
        self.next = None

class ArvoreBinaria:
    def __init__(self, data=None):
        node = Node(data)
        self.raiz = node
        
    def root(self, node):
        node = Node(node)
        self.raiz = node
    
    def insertleft(self, node, node_pai):
        node_pai.left = node

    def insertright(self, node, node_pai):
        node_pai.right = node

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

def postorder(raiz):
    no = raiz
    pilha = Pilha()
    while True:
        while (no):
                if no.right is not None:
                    pilha.push(no.right)
                pilha.push(no)
               
                no = no.left
         
        no = pilha.pop()
        if (no.right is not None and pilha.peek() == no.right):
                pilha.pop()
                pilha.push(no)
                no = no.right
        else:
            print(no.data, end=" ")
            no = None
            
        if pilha._size <= 0:
            break  
            
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
tree.insertleft(node12, node7)


# In[2]:


inorder(raiz)


# In[3]:


postorder(raiz)


# In[ ]:




