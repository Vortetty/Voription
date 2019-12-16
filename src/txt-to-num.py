import math

def tonum( p ):
  pswd = []
  pswd[:0] = p
  result = ""
  print(pswd)
  for i in range(len(pswd)): 
    num = ord(pswd[i])
    result += str(num)
  return result

def getpass():
  password = input("Enter password containing only ASCII characters: ")
  if(password.isascii() == True):
    key = tonum(password)
  elif(password.isascii() == False):
    print("Password contains non-ASCII Characters, Please try again")
    getpass()
  print(key)
