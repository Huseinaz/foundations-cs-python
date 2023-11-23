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

  def __init__(self, name, midterm_grade, final_grade, good_attitude):
    self.name = name
    self.midterm_grade = midterm_grade
    self.final_grade = final_grade
    self.good_attitude = good_attitude

  # def getName(self):
  #   return self.name
  # def getmidtermGrade(self):
  #   return self.midterm_grade
  # def getFinalGrade(self):
  #   return self.final_grade
  # def getGoodAttitude(self):
  #   return self.good_attitude

  # def setName(self, new_name):
  #   self.name = new_name
  # def setMidtermGrade(self, new_midterm_grade):
  #   self.midterm_grade = new_midterm_grade
  # def setFinalGrade(self, new_final_grade):
  #   self.final_grade = new_final_grade
  # def setGoodAttitude(self, new_good_attitude):
  #   self.good_attitude = new_good_attitude

def addStudent():
  name = input("Enter student name: ")
  midterm_grade = int(input("Enter midterm grade: "))
  final_grade = int(input("Enter final grade: "))
  good_attitude = bool(input("Enter good attitude: "))

  new_student = Student(name, midterm_grade, final_grade, good_attitude)
  return new_student

  # print(self.name,", midterm_grade: ",self.midterm_grade,"/100, final_grade: ", self.final_grade,"/100, good_attitude: ", self.good_attitude, sep='')

class Node:

  def __init__(self, student):
    self.student = student
    self.next = None

class PriorityQueue:

  def __init__(self):

    self.head = None
    self.size = 0

  def displayNodes(self):

    current = self.head
    while current != None:
      print(current.student.name,", midterm_grade: ",current.student.midterm_grade,"/100, final_grade: ", current.student.final_grade,"/100, good_attitude: ", current.student.good_attitude, sep='')
      current = current.next

  def enqueue(self, student):

    node = Node(student)
    if self.size == 0:
      self.head = node
      self.size += 1
    else:
      current = self.head
      previous = None
      while current != None and current.student.good_attitude:
        if student.final_grade > self.head.student.final_grade:
          break
        elif student.final_grade == self.head.student.final_grade:
          if student.midterm_grade > self.head.student.midterm_grade:
            break
        previous = current
        current = current.next
        self.size += 1
      else:
        current = self.head
        previous = current #we can remove this
        while current != None and current.student.final_grade <= student.final_grade:
          previous = current
          current = current.next
        previous.next = node
        node.next = current
        self.size += 1

  def dequeue(self):

    if self.size == 0:
      print("Your queue is empty, enqueue first.")
    elif self.size == 1:
      print("Interview with: ", self.head.student.name)
      self.head = None
      self.size -=1
    else:
      print("Interview with: ", self.head.student.name)
      current = self.head
      self.head = self.head.next
      current.next = None
      self.size -= 1

pq = PriorityQueue()

######################################################################################

class EvaluateString: #https://stackoverflow.com/questions/43649924/infix-evaluation-in-python

  def evalString(self,expression):
    valueStack = []
    opStack = []
    i=0

    while(i<len(expression)):
      if(expression[i] == ' '):
        continue
      if(expression[i]>='0' and expression[i] <= '9'):
        charNumber = [] #for storing number
        j = i
        while(j<len(expression) and expression[j]>='0' and expression[j] <= '9'):
          charNumber.append(expression[j])
          j += 1

        i = (j-1)
        valueStack.append(int(''.join(charNumber)))

      elif (expression[i]=='('):
        opStack.append(expression[i])

      elif (expression[i]==')'):
        while(opStack[-1]!='('):
          valueStack.append(self.applyOperation(opStack.pop(),valueStack.pop(),valueStack.pop()))
        opStack.pop()
      elif(expression[i]=='+'or expression[i]=='-'or expression[i]=='*'or expression[i]=='/'):
        while( (len(opStack)!=0) and ( self.opPrecedence(expression[i],opStack[-1]) ) ):
          valueStack.append(self.applyOperation(opStack.pop(),valueStack.pop(),valueStack.pop()))
        opStack.append(expression[i])
      i = i + 1

    while(len(opStack)!=0):
      valueStack.append(self.applyOperation(opStack.pop(),valueStack.pop(),valueStack.pop()))

    return valueStack.pop()


  def applyOperation(self,op,a,b):
    if op=='+':
      return a+b
    elif op=='-':
      return b-a
    elif op=='*':
      return a*b
    elif op=='/':
      return b/a
    else:
      return 0

  def opPrecedence(self,op1,op2):
    if (op2 == '(' or op2 == ')'):
      return False
    if ((op1 == '*' or op1 == '/') and (op2 == '+' or op2 == '-')):
      return False
    else:
      return True

es = EvaluateString()

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
      choice = ''
      while choice != 'c':
        choice = input("\nChoose a letter from the menu: ")
        if choice == 'a':
          pq.enqueue(addStudent())
          pq.displayNodes()
        elif choice == 'b':
          pq.dequeue()
        elif choice != 'c':
          print("Invalid input.")
        choice == 3
    elif choice == 4:
      str = input("Enter a string infix expression to evaluate : ")
      print(es.evalString(str))
      
menu()