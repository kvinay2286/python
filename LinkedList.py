#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 02:45:55 2018

@author: kvinay
"""

class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node
    def __repr__(self):
        return ("Node: {} Next: {}".format(self.data, self.next))

#n1 = Node(1, None)
#n2 = Node(2, n1)

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    
    def printList(self):
        curr = self.head
        while curr is not None:
            print("{} --> ".format(curr.data), end='')
            curr = curr.next
        print('None\n')
    
    def insertAtHead(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def reverseLinkedList(self):
        if self.head is None:
            return
        else:
            prev = None
            curr = self.head
            while curr is not None:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            self.head = prev

    def deleteNode(self, data):
        if self.head is None:
            return
        else:
            curr = self.head
            prev = None
            while curr is not None and curr.data != data:
                prev = curr
                curr = curr.next
            prev.next = curr.next
            del curr
                
    
    def searchNode(self, data):
        while self.head is not None:
            if self.data == data:
                print(True)
            else:
                print(False)
            self.head = self.next
    
    def insertAtEnd(self, data):
        node = Node(data)
        if self.head is None:
            return
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node
            
                
            

#TEST main()           
ll =  LinkedList()
ll.insertAtHead(3)     
ll.insertAtHead(2) 
ll.insertAtHead(1) 
ll.insertAtEnd(4)
ll.printList()
ll.deleteNode(2)  
ll.printList()
#ll.reverseLinkedList()
#ll.printList()



