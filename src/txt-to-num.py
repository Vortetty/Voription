import math
import os
import textwrap
import binascii

# get rows and columns for size calculations
rows, columns = os.popen('stty size', 'r').read().split()
wrapper = textwrap.TextWrapper(width = int(columns))

def tonum( p ):
  pswd = []
  pswd[:0] = p
  result = ""
  #print(pswd)
  for i in range(len(pswd)): 
    num = ord(pswd[i])
    if(num==32):
      num = "25752"
    result += str(num)
  return result

def getpass():

  password = input(wrapper.fill("Enter password containing only ASCII characters: "))

  if(password.isascii() == True):
    key = tonum(password)
    print(wrapper.fill("Keep track of this password, you will need it to retrieve files later: " + "'" + password + "'"))

  elif(password.isascii() == False):
    print(wrapper.fill("\nPassword contains non-ASCII Characters, Please try again."))
    getpass()

  return key

def getfile():
  f = input(wrapper.fill("what file would you like to encrypt? must be in the same directory this script is run from, or be an absolute path starting from the root directory: "))
  return f

image_file = getfile()
fin = open(image_file, "rb")
data = fin.read()

def bits():
  # convert every byte of data to the corresponding 2-digit hexadecimal
  hex_str = str(binascii.hexlify(data))
  # now create a list of 2-digit hexadecimals
  hex_list = []
  bin_list = []
  for ix in range(2, len(hex_str)-1, 2):
      hex = hex_str[ix]+hex_str[ix+1]
      hex_list.append(hex)
      bin_list.append(bin(int(hex, 16))[2:])
  #print(bin_list)
  bin_str = "".join(bin_list)
  print(bin_str)

key = getpass()
