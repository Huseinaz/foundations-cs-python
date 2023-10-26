print("\nQuestion 1: \n")

def reverseFunction(s,i):
  if i == 0:
    return ""
  return s + reverseFunction(s,i-1)

text = input("Enter the text to reverse: ")
num = int(input("Enter how may time you want to print the reversed text: "))
print(reverseFunction(text[::-1],num))

print("\nQuestion 2: \n")

def arrangeFunction(s):
  uppercase_chars = ""
  lowercase_chars = ""
  for char in s:
    if char.isupper():
      uppercase_chars += char
    elif char.islower():
      lowercase_chars += char
  return uppercase_chars + lowercase_chars

text = input("Enter a text: ")
print(arrangeFunction(text))

print("\nQuestion 3: \n")

def reorderingFunction(s1,s2):
  return sorted(s1) == sorted(s2)

text1 = input("Enter text 1: ")
text2 = input("Enter text 2: ")
print(reorderingFunction(text1,text2))

print("\nQuestion 4: \n")

def maxFunction(list):
  maximum = list[0]
  for num in range(len(list)):
    if list[num] > maximum:
      maximum = list[num]
  return maximum

list = [5,6,3,2,7,2,0,1,6]
print("The maximum number in the list is:",maxFunction(list))

print("\nQuestion 5: \n")

def sumFunction(n):
  if n//10 == 0:
    return n
  return n%10 + sumFunction(n//10)

num = int(input("Enter a number: "))
print("The sum of recursive number is:",sumFunction(num))
  
print("\nQuestion 6: \n")

def removeConsecutiveDuplicate(s):
  if len(s) == 0:
    return ""
  if len(s) == 1:
    return s
  if s[0] == s[1]:
    return removeConsecutiveDuplicate(s[1:])
  return s[0] + removeConsecutiveDuplicate(s[1:])
  
text = input("Enter a text: ")
print(removeConsecutiveDuplicate(text))

print("\nQuestion 7: \n")

def reverseFunction(n):
  if n//10 == 0:
    return n
  last_digit = n % 10
  remaining_num = n//10
  return int(str(last_digit) + str(reverseFunction(remaining_num)))

num = int(input("Enter a number: "))
print("The reversed number is:", reverseFunction(num))