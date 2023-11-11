import requests
open_tabs = []

def openTab():
  title = input("Enter the title of the tab: ")
  url = input("Enter the url of the website: ")
  tab = {"Title":title,"URL":url}
  open_tabs.append(tab)
  print("The opened tabs are",open_tabs)

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

def switchTab():
  if len(open_tabs) == 0:
    print("No tabs are open.")
  else:
    tab_to_switch = input("Enter the title of the tab you want to switch to: ")
    if tab_to_switch == '':
      r = requests.get(open_tabs[-1]['URL']) #reference: https://www.geeksforgeeks.org/python-web-scraping-tutorial/
      print(r.content)
    else:
      for tab in open_tabs:
        if tab_to_switch == tab["Title"]:
          r = requests.get(tab['URL'])
          print(r.content)
          break
      if tab_to_switch != tab["Title"]:
          print("The tab",tab_to_switch,"is not found")

######################################################################################

def clearAllTab():
  if len(open_tabs) == 0:
    print("No tabs are open.")
  else:
    open_tabs.clear() #reference: https://www.programiz.com/python-programming/methods/list/clear
    print("All tabs are closed")


######################################################################################

print("Welcome!")

def displayMenu():
  print("\n\t1. Open Tab\n"
        +"\t2. Close Tab\n"
        +"\t3. Switch Tab\n"
        +"\t4. Display All Tabs\n"
        +"\t5. Open Nested Tab\n"
        +"\t6. Clear All Tabs\n"
        +"\t7. Save Tabs\n"
        +"\t8. Import Tabs\n"
        +"\t9. Exit\n")

def menu():
  choice = 0
  while choice != 7:
    displayMenu()
    choice = int(input("Choose a number from the menu: "))
    if choice == 1:
        openTab()
    elif choice == 2:
        closeTab()
    elif choice == 3:
        switchTab()
    elif choice == 6:
        clearAllTab()


menu()