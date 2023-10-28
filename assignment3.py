def addMatrices():
  matrix1 = []
  matrix2 = []
  num_rows = int(input("Enter the number of rows: "))
  num_cols = int(input("Enter the number of columns: "))
  sum_matrix = []
  
  for row in range(num_rows):
    matrix1.append([])
    print("Enter elements of row",row+1,"of the first matrix:")
    for col in range(num_cols):
      col = int(input())
      matrix1[row].append(col)

  for row in range(num_rows):
    matrix2.append([])
    print("Enter elements of row",row+1,"of the second matrix:")
    for col in range(num_cols):
      col = int(input())
      matrix2[row].append(col)

  for row in range(num_rows):
    sum_row = [matrix1[row][col] + matrix2[row][col] for col in range(num_cols)]
    sum_matrix.append(sum_row)

  print(matrix1,"+",matrix2,"=",sum_matrix)

######################################################################################

def invertDictionary():
  dict = {}
  num_entries = int(input("Enter the number of dictionary entries: "))

  for i in range(num_entries):
    key = input("Enter a key: ")
    value = input("Enter a value: ")
    dict[key] = value
  
  print("Before inverting:")
  print(dict)

  inverted_dict = {}
  
  for key,value in dict.items():
    if value not in inverted_dict:
      inverted_dict[value] = [key]
    else:
      inverted_dict[value].append(key)

  print("After inverting:")
  print(inverted_dict)

  ######################################################################################

def matrixToDictionary():
  users_data = []
  num_users = int(input("Enter the number of the users: "))

  for row in range(num_users):
    print("User",row)
    firstName = input("Enter the first name: ")
    lastName = input("Enter the last name: ")
    id = input("Enter the id: ")
    jobTitle = input("Enter the job title: ")
    company = input("Enter the company: ")
    users_data.append([firstName, lastName, id, jobTitle, company])
  print(users_data)


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
    addMatrices()
  elif choice == 2:
    print("Check Rotation")
  elif choice == 3:
    invertDictionary()
  elif choice == 4:
    matrixToDictionary()
menu()