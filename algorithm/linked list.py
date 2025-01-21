class node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=node(10)
node2=node(20)
node3=node(30)
node1.next=node2
node2.next=node3
cn=node1
while cn!=None:
    print(cn.data,end=" ")
    cn=cn.next
print(cn)