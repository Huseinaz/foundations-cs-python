open_tabs = []

def openTab():
  title = input("Enter the title of the tab: ")
  url = input("Enter the url of the website: ")
  tab = {"Title":title,",URL":url}
  open_tabs.append(tab)

######################################################################################

def closeTab():
  if len(open_tabs) == 0:
    print("No tabs are open.")

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
  elif choice == 2:
    print("Close Tab")

menu()