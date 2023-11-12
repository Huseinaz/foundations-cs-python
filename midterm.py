import requests
import pandas as pd
import csv
import json
import os

#Empty list of opened taps
open_tabs = []

def openTab(): #O(1) constant
  #ask the user for the data of the tab
  title = input("Enter the title of the tab: ")
  url = input("Enter the url of the website: ")
  #create dict of tabs includes title and url
  tab = {"Title":title,"URL":url}
  #adding tab dict to the list of opened tabs
  open_tabs.append(tab)
  print("The opened tabs are",open_tabs)

######################################################################################

def closeTab(): #O(n)
  #check if no tabs are open 
  if len(open_tabs) == 0: #O(1)
    print("No tabs are open.")
  else:
    #ask the user for the title of tab he want to close
    tab_to_close = input("Enter the title of the tab you want to close: ")
    #if no title is provided the system will close the last opened tab.
    if tab_to_close == '': #O(1)
      print("The tab",open_tabs[-1]['Title'],"is closed")
      open_tabs.remove(open_tabs[-1])
    else:
      for tab in open_tabs: #O(n)
        if tab_to_close == tab["Title"]:
          #close the tab with title entered
          print("The tab",tab_to_close,"is closed")
          open_tabs.remove(tab)
      if tab_to_close != tab["Title"]: #O(1)
        #no tabs with title of the title entered
        print("The tab",tab_to_close,"is not found")

######################################################################################

def switchTab(): #O(n)
  #check if no tabs are open
  if len(open_tabs) == 0: #O(1)
    print("No tabs are open.")
  else:
    #ask the user for the title of tab he want to switch to
    tab_to_switch = input("Enter the title of the tab you want to switch to: ")
    #if no title is provided the system will switch to the last opened tab.
    if tab_to_switch == '': #O(1)
      #function to get the HTML content of url
      r = requests.get(open_tabs[-1]['URL']) #reference: https://www.geeksforgeeks.org/python-web-scraping-tutorial/
      print(r.content)
    else:
      for tab in open_tabs: #O(n)
        if tab_to_switch == tab["Title"]:
          #switch to the tab with title entered and get the HTML content of url
          r = requests.get(tab['URL'])
          print(r.content)
          break
      if tab_to_switch != tab["Title"]: #O(1)
          #no tabs with title of the title entered
          print("The tab",tab_to_switch,"is not found")

######################################################################################

def displayAllTabs(): #O(n)
  #check if no tabs are open
  if len(open_tabs) == 0: #O(1)
    print("No tabs are open")
  else:
    print("The title of opened tabs are:") #O(1)
    for tab in open_tabs: #O(n)
      #print the titles of all open tabs
      title = tab["Title"]
      print(title)

######################################################################################

def openNestedTab(): #O(n)
  #ask the user for the title of the parent tab
  title = input("Enter the title of the parent tab: ")
  for tab in open_tabs: #O(n)
    if tab['Title'] == title: #O(1)
      #if tab is found asks the user for title and content of nasted tab
      title = input("Enter the title of the nested tab: ")
      content = input("Enter the content of the nested tab: ")
      #create dict nested tab  and insert it to open_tabs list
      nested_tab = {"Title":title,"Content":content}
      open_tabs.insert(len(title)-1,nested_tab) #O(n) .insert() runtime by google #https://www.programiz.com/python-programming/methods/list/insert
      break
  else: #O(1)
    ##no parent with title of the title entered
    print("No title found with this name.")

######################################################################################

def clearAllTab(): #O(n)
  #check if no tabs are open
  if len(open_tabs) == 0: #O(1)
    print("No tabs are open.")
  else:
    #clear all tabs opened
    open_tabs.clear() #O(n) .clear() runtime by google #reference: https://www.programiz.com/python-programming/methods/list/clear
    print("All tabs are closed")

######################################################################################

def saveTabs(file_path): #O(1)
  #save the current state to file that user entered
  with open(os.path.join(file_path), "w") as file: #https://stackoverflow.com/questions/25778021/how-can-i-save-a-list-of-dictionaries-to-a-file
    #info written to the file in JSON format.
    file.write(json.dumps(open_tabs, indent=4)) #https://stackoverflow.com/questions/8024248/telling-python-to-save-a-txt-file-to-a-certain-directory-on-windows-and-mac

######################################################################################  

def importTabs(file_path): #O(1)
  #save the data from file that user entered
  data = pd.read_csv(file_path) #reference: https://www.youtube.com/watch?v=9xcY6YDu-Ks
  #adding data to to open_tabs list
  open_tabs.append(data)

######################################################################################

#greeting the user
print("Welcome!")

#create the following menu
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
    #display the menu
    displayMenu()
    #ask the user to enter a number from the menu to run the content
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
        #ask the user to provide a file path
        file_path = input("Enter the file path to save the tabs to: ")
        saveTabs(file_path)
    elif choice == 8:
        #ask the user to provide a file path
        file_path = input("Enter the file path to import from: ")
        importTabs(file_path)
  #the user press 9 (exit the menu)
  print("You exit the menu")

menu()