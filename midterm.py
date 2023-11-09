def openTab():
  title = input("Enter the title of the tab: ")
  url = input("Enter the url of the website: ")
  print("The title of tab is",title,"with URL",url)

######################################################################################

print("Welcome!")
print()

def displayMenu():
  print("\t1. Open Tab\n"
        +"\t2. Close Tab\n"
        +"\t3. Switch Tab\n"
        +"\t4. Display All Tabs\n"
        +"\t5. Open Nested Tab\n"
        +"\t6. Clear All Tabs\n"
        +"\t7. Save Tabs\n"
        +"\t8. Import Tabs\n"
        +"\t9. Exit\n")

displayMenu()

def menu():
  choice = int(input("\nChoose a number from the menu: "))
  if choice == 1:
    openTab()

menu()