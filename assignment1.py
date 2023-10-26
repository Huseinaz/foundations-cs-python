print("\nQuestion 1: \n")

a = 10*(90+2)-5          #10*(92)-5 => 920-5 => 915
b = 10*90+2-5            #900+2-5 => 902-5 => 897
c = 10*90+(2-5)          #10*90-3 => 900-3 => 897
d = 10.0*(90+2)-5        #10.0*92-5 => 920.0-5 => 915.0
e = 120/(20+40)-(6-2)/4  #120/60-4/4 => 2.0-1.0 => 1.0
f = 5.0/2                #2.5
g = 5/2                  #2.5
h = 5.0/2.0              #2.5
i = 5/2.0                #2.5
j = 678%3*(8-(9/4))      #0*(8-2.25) => 0*5.75 => 0.0

print("10*(90+2)-5 =", a ,
      "\n10*90+2-5 =", b ,
      "\n10*90+(2-5) =", c ,
      "\n10.0*(90+2)-5 =", d ,
      "\n120/(20+40)-(6-2)/4 =", e ,
      "\n5.0/2 =", f ,
      "\n5/2 =", g ,
      "\n5.0/2.0 =", h ,
      "\n5/2.0 =", i ,
      "\n678%3*(8-(9/4)) =", j
     )

print("\nQuestion 2: \n")

user_id = input("Enter your ID: ")
user_id = "0" + user_id
print("The ID is:", user_id)

user_name = input("Enter your name: ").upper()
print("The name is:", user_name)

user_dob = input("Enter your date of birth: ")
for x in range(len(user_dob)):
  if user_dob[x] == "-":
    user_dob = user_dob[:x] + "/" + user_dob[x+1:]
print("The date of birth is:", user_dob)

user_address = input("Enter your address: ").lower().strip()
print("The address is:", user_address)

print("\nQuestion 3: \n")

number = input("Enter a number: ")
length = len(number)
print(number,"has", length ,"digits")

print("\nQuestion 4: \n")

grade = int(input("Enter your grade: "))
letter_grade = ""

if grade >= 97:
  letter_grade = "A+"
elif grade >= 93:
  letter_grade = "A"
elif grade >= 90:
  letter_grade = "A-"
elif grade >= 87:
  letter_grade = "B+"
elif grade >= 83:
  letter_grade = "B"
elif grade >= 80:
  letter_grade = "B-"
elif grade >= 87:
  letter_grade = "B+"
elif grade >= 83:
  letter_grade = "B"
elif grade >= 80:
  letter_grade = "B-"
elif grade >= 77:
  letter_grade = "C+"
elif grade >= 73:
  letter_grade = "C"
elif grade >= 70:
  letter_grade = "C-"
elif grade >= 67:
  letter_grade = "D+"
elif grade >= 63:
  letter_grade = "D"
elif grade >= 60:
  letter_grade = "D-"
else:
  letter_grade = "F"
print("Your grade is:", letter_grade)

print("\nQuestion 5: \n")

n = int(input("Enter a number: "))
for i in range(n+1):
  print("*"*i)
  i+=1
for j in range(n-1,0,-1):
  print("*"*j)
  j+=1

print("\nQuestion 6: \n")

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

while(n1>n2):
  print("The second number cannot be smaller than first number.")
  break
else:
  n=n1
  while(n<n2):
    n+=1
    if n%2==0:
      print(n)