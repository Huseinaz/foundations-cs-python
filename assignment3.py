name = input("Please enter your name: ")
print("Welcome",name,"!")

def displayMenu():
  print("\n\t1. Add Matrices\n"
        +"\t2. Check Rotation\n"
        +"\t3. Invert Dictionary\n"
        +"\t4. Convert Matrix to Dictionary\n"
        +"\t5. Check Palindrome\n"
        +"\t6. Search for an Element & Merge Sort\n"
        +"\t7. Exit\n")

displayMenu()

def menu():
  choice = eval(input("\nChoose a number from the menu: "))
  if choice == 1:
    print("Add Matrices")
  
menu()