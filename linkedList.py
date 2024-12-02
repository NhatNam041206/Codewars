class node:
    def __init__ (self, data=None):
        self.data=data
        self.next=None
    

class linkedList:
    def __init__(self):
        self.head=node()

    def append(self, data):
        newData=node(data)
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=newData
    def length(self):
        cur=self.head
        lengthL=0
        while cur.next!=None:
            lengthL+=1
            cur=cur.next
        return lengthL
    
    def erase(self,index):
        if index>=self.length() or index<0: # added 'index<0' post-video
            print("ERROR: 'Erase' Index out of range!")
            return 
        cur_idx=0
        cur_node=self.head
        while True:
            last_node=cur_node
            cur_node=cur_node.next
            if cur_idx==index:
                last_node.next=cur_node.next
                return
            cur_idx+=1

    def insert(self,index,data):
        if index>=self.length() or index<0:
            return self.append(data)
        cur_node=self.head
        prior_node=self.head
        cur_idx=0
        while True:
            cur_node=cur_node.next
            if cur_idx==index: 
                new_node=node(data)
                prior_node.next=new_node
                new_node.next=cur_node
                return
            prior_node=cur_node
            cur_idx+=1


    def display(self):
        elems=[]
        cur=self.head
        while cur.next!=None:
            cur=cur.next
            elems.append(cur.data)
            
        print(elems)

a=linkedList()
a.append(1)
a.append('as')
a.append(None)
a.append([1,2,34])
a.erase(2)
a.insert(1,'op')
a.display()