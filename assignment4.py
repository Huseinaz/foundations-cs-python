class Node:

  def __init__(self, info):
    
    self.info = info
    self.next = None

class LinkedList:

  def __init__(self):
    
    self.head = None
    self.size = 0

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
  
displayMenu()

def menu():
  choice = 0
  while choice != 6:
    choice = eval(input("\nChoose a number from the menu: "))
    if choice == 1:
      print("\n\ta. Add Node\n"
            +"\tb. Display Nodes\n"
            +"\tc. Search for & Delete Node\n"
            +"\td. Return to main menu\n")
      choice = input("\nChoose a letter from the menu: ")
      if choice == 'a':
        ll.addNode()
      if choice == 'b':
        print("Display Nodes")
      
menu()