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

class Stack:

  def __init__(self):
    self.head = None
    self.size = 0

  def isEmpty(self):
    return self.head == None

  def push(self, value): #to add to the stack
    node = Node(value)
    node.next = self.head
    self.head = node
    self.size += 1

  def pop(self): #to remove element from the the top of the stack
    if self.size == 0: #self.isEmpty():
      print("Cannot pop from an empty stack!")
    else:
      current = self.head
      self.head = self.head.next
      current.next = None
      self.size -= 1
      return current.info

  def palindrome(s):
    stack = Stack()
    for i in range(len(s)):
      stack.push(s[i])
    rev_str = ''
    while not stack.isEmpty():
      rev_str += stack.pop()
    if s == rev_str:
      return "Palindrome"
    else:
      return "Not a palindrome"

######################################################################################

class Student:

  def __init__(self, name, mideterm_grade, final_grade, good_attitude):
    self.name = name
    self.mideterm_grade = mideterm_grade
    self.final_grade = final_grade
    self.good_attitude = good_attitude

def addStudent(self):
  self.name = input("Enter student name: ")
  self.mideterm_grade = int(input("Enter mideterm grade: "))
  self.final_grade = int(input("Enter final grade: "))
  self.good_attitude = bool(input("Enter good attitude: "))

  print(self.name,", midterm_grade: ",self.mideterm_grade,"/100, final_grade: ", self.final_grade,"/100, good_attitude: ", self.good_attitude, sep='')

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
      s = input("Enter a string: ")
      print(Stack.palindrome(s))
    elif choice == 3:
      print("\n\ta. Add a student\n"
            +"\tb. Interview a student\n"
            +"\tc. Return to main menu\n")
      choice = input("\nChoose a letter from the menu: ")
      if choice == 'a':
        addStudent(Student)
      
menu()