import requests
import pandas as pd
import csv
import json
import os

open_tabs = []

def openTab(): #O(1) constant
  title = input("Enter the title of the tab: ")
  url = input("Enter the url of the website: ")
  tab = {"Title":title,"URL":url}
  open_tabs.append(tab)
  print("The opened tabs are",open_tabs)

######################################################################################

def closeTab(): #O(n)
  if len(open_tabs) == 0: #O(1)
    print("No tabs are open.")
  else:
    tab_to_close = input("Enter the title of the tab you want to close: ")
    if tab_to_close == '': #O(1)
      print("The tab",open_tabs[-1]['Title'],"is closed")
      open_tabs.remove(open_tabs[-1])
    else:
      for tab in open_tabs: #O(n)
        if tab_to_close == tab["Title"]:
          print("The tab",tab_to_close,"is closed")
          open_tabs.remove(tab)
      if tab_to_close != tab["Title"]: #O(1)
        print("The tab",tab_to_close,"is not found")

######################################################################################

def switchTab(): #O(n)
  if len(open_tabs) == 0: #O(1)
    print("No tabs are open.")
  else:
    tab_to_switch = input("Enter the title of the tab you want to switch to: ")
    if tab_to_switch == '': #O(1)
      r = requests.get(open_tabs[-1]['URL']) #reference: https://www.geeksforgeeks.org/python-web-scraping-tutorial/
      print(r.content)
    else:
      for tab in open_tabs: #O(n)
        if tab_to_switch == tab["Title"]:
          r = requests.get(tab['URL'])
          print(r.content)
          break
      if tab_to_switch != tab["Title"]: #O(1)
          print("The tab",tab_to_switch,"is not found")

######################################################################################

def displayAllTabs(): #O(n)
  if len(open_tabs) == 0: #O(1)
    print("No tabs are open")
  else:
    print("The title of opened tabs are:") #O(1)
    for tab in open_tabs: #O(n)
      title = tab["Title"]
      print(title)

######################################################################################

def openNestedTab(): #O(n)
  title = input("Enter the title of the parent tab: ")
  for tab in open_tabs: #O(n)
    if tab['Title'] == title: #O(1)
      title = input("Enter the title of the nested tab: ")
      content = input("Enter the content of the nested tab: ")
      nested_tab = {"Title":title,"Content":content}
      open_tabs.insert(len(title)-1,nested_tab) #O(n) .insert() runtime by google #https://www.programiz.com/python-programming/methods/list/insert
      break
  else: #O(1)
    print("No title found with this name.")

######################################################################################

def clearAllTab(): #O(n)
  if len(open_tabs) == 0: #O(1)
    print("No tabs are open.")
  else:
    open_tabs.clear() #O(n) .clear() runtime by google #reference: https://www.programiz.com/python-programming/methods/list/clear
    print("All tabs are closed")

######################################################################################

def saveTabs(file_path): #O(1)
  with open(os.path.join(file_path), "w") as file: #https://stackoverflow.com/questions/25778021/how-can-i-save-a-list-of-dictionaries-to-a-file
    file.write(json.dumps(open_tabs, indent=4)) #https://stackoverflow.com/questions/8024248/telling-python-to-save-a-txt-file-to-a-certain-directory-on-windows-and-mac

######################################################################################  

def importTabs(file_path): #O(1)
  data = pd.read_csv(file_path) #reference: https://www.youtube.com/watch?v=9xcY6YDu-Ks
  open_tabs.append(data)

######################################################################################

print("Welcome!")

def displayMenu(): #O(1) constant
  print("\n\t1. Open Tab\n"
        +"\t2. Close Tab\n"
        +"\t3. Switch Tab\n"
        +"\t4. Display All Tabs\n"
        +"\t5. Open Nested Tab\n"
        +"\t6. Clear All Tabs\n"
        +"\t7. Save Tabs\n"
        +"\t8. Import Tabs\n"
        +"\t9. Exit\n")

def menu(): #O(1)
  choice = 0
  while choice != 9:
    displayMenu()
    choice = int(input("Choose a number from the menu: "))
    if choice == 1:
        openTab()
    elif choice == 2:
        closeTab()
    elif choice == 3:
        switchTab()
    elif choice == 4:
        displayAllTabs()
    elif choice == 5:
        openNestedTab()
    elif choice == 6:
        clearAllTab()
    elif choice == 7:
        file_path = input("Enter the file path to save the tabs to: ")
        saveTabs(file_path)
    elif choice == 8:
        file_path = input("Enter the file path to import from: ")
        importTabs(file_path)
  print("You exit the menu")


menu()