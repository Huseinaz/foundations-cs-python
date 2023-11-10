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
  else:
    tab_to_close = input("Enter the title of the tab you want to close: ")
    if tab_to_close == '':
      print("The tab",open_tabs[-1]['Title'],"is closed")
      open_tabs.remove(open_tabs[-1])
    else:
      for tab in open_tabs:
        if tab_to_close == tab["Title"]:
          print("The tab",tab_to_close,"is closed")
          open_tabs.remove(tab)
      if tab_to_close != tab["Title"]:
        print("The tab",tab_to_close,"is not found")

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
    closeTab()

menu()