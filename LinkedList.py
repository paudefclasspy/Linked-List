class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linkedlist():
    def __init__(self):
        self.head = node()

    def append(self,data):
        newNode = node(data)
        lookingat = self.head
        while lookingat.next != None:
            lookingat = lookingat.next
        lookingat.next = newNode

    def len(self):
        lookingat = self.head
        total = 0
        while lookingat.next != None:
            total +=1
            lookingat = lookingat.next
        return total

    def display(self):
        elements = []
        lookingnode = self.head
        while lookingnode.next!=None:
            lookingnode = lookingnode.next
            elements.append(lookingnode.data)
        print (elements)

    def get(self,index):
        if index >=self.len():
            print("ERROR")
            return None
        lookingindex = 0
        lookingnode =self.head
        while True:
            lookingnode=lookingnode.next
            if lookingindex==index: return lookingnode.data
            lookingindex+=1

list = linkedlist()
list.append(1)
list.append(2)
list.append(3)
list.append(4)

list.display()

print("Element en el segundo index ", list.get(2))