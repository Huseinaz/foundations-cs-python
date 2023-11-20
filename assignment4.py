class Node:

  def __init__(self, info):
    
    self.info = info
    self.next = None

class LinkedList:

  def __init__(self):
    
    self.head = None
    self.size = 0

######################################################################################

  def displayNodes(self):
    current = self.head
    while current != None:
      print(current.info, end=" ")
      current = current.next
    print()

######################################################################################

  def addNode(self):
    
    value = int(input("Enter the node value: "))
    node = Node(value)
    if self.size == 0:
      self.head = node
      self.size += 1
    else:
      current = self.head #https://www.geeksforgeeks.org/insertion-in-linked-list/
      while (current.next):
          current = current.next
      current.next = node

######################################################################################

  def removeNode(self): #https://www.geeksforgeeks.org/python-program-for-deleting-a-node-in-a-linked-list/
    
    if self.size == 0:
      print("Linked List is empty.")
    else:
      value = int(input("Enter the number to delete from the list: "))
      temp = self.head  
      if (temp is not None): 
        if (temp.info == value): 
          self.head = temp.next
          temp = None
          return
      while(temp is not None): 
        if temp.info == value: 
          break
        prev = temp 
        temp = temp.next
      if(temp == None): 
        return
      prev.next = temp.next
      temp = None

ll = LinkedList()

######################################################################################


name = input("Please enter your name: ")
print("Welcome",name,"!")

def displayMenu():
  print("\n\t1. Singly Linked List\n"
        +"\t2. Check if Palindrome\n"
        +"\t3. Priority Queue\n"
        +"\t4. Evaluate an Infix Expression\n"
        +"\t5. Graph\n"
        +"\t6. Exit\n")

def menu():
  choice = 0
  while choice != 6:
    displayMenu()
    choice = eval(input("\nChoose a number from the menu: "))
    if choice == 1:
      print("\n\ta. Add Node\n"
            +"\tb. Display Nodes\n"
            +"\tc. Search for & Delete Node\n"
            +"\td. Return to main menu\n")
      choice = ''
      while choice != 'd':
        choice = input("\nChoose a letter from the menu: ")
        if choice == 'a':
            ll.addNode()
        elif choice == 'b':
            ll.displayNodes()
        elif choice == 'c':
            ll.removeNode()
        elif choice != 'd':
            print("Invalid input.")
        choice == 1
    elif choice == 2:
      print("Check if Palindrome")
      
menu()