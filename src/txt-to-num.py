"""
 __      __                    _   _                                          
 \ \    / /                   | | (_)                                         
  \ \  / /__  _ __ _   _ _ __ | |_ _  ___  _ __                               
   \ \/ / _ \| '__| | | | '_ \| __| |/ _ \| '_ \                              
    \  / (_) | |  | |_| | |_) | |_| | (_) | | | |                             
     \/ \___/|_|   \__, | .__/ \__|_|\___/|_| |_|                             
                    __/ | |                                                   
                   |___/|_|                                                   
    ________     ___   ___  __  ___   __      __        _       _   _         
   /  ____  \   |__ \ / _ \/_ |/ _ \  \ \    / /       | |     | | | |        
  /  / ___|  \     ) | | | || | (_) |  \ \  / /__  _ __| |_ ___| |_| |_ _   _ 
 |  | |       |   / /| | | || |\__, |   \ \/ / _ \| '__| __/ _ \ __| __| | | |
 |  | |___    |  / /_| |_| || |  / /     \  / (_) | |  | ||  __/ |_| |_| |_| |
  \  \____|  /  |____|\___/ |_| /_/       \/ \___/|_|   \__\___|\__|\__|\__, |
   \________/                                                            __/ |
                                                                        |___/

  This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
  To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

  To obtain rights to use this commecially (if you want to for some reason, contact me on reddit /u/vortetty
  
"""

import math
import os
import textwrap
import binascii
import shutil

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
  password = input("Enter password containing only ASCII characters: ")

  if(password.isascii() == True):
    key = tonum(password)
    print("Keep track of this password, you will need it to retrieve files later: " + "'" + password + "'")
    
  elif(password.isascii() == False):
    print("\nPassword contains non-ASCII Characters, Please try again.")
    getpass()

  return key

def getpassdec():
  password = input("Enter password for file containing only ASCII characters: ")

  if(password.isascii() == True):
    key = tonum(password)
    
  elif(password.isascii() == False):
    print("\nPassword contains non-ASCII Characters, Please try again.")
    getpassdec()

  return key

def getfile():
  f = input("what file would you like to encrypt? must be in the same directory this script is run from, or be an absolute path starting from the root directory: ")
  return f

def getfiledec():
  f = input("what file would you like to decrypt? must be in the same directory this script is run from, or be an absolute path starting from the root directory: ")
  return f

def bits(data):
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
  return bin_str

def hexer(data):
  # convert every byte of data to the corresponding 2-digit hexadecimal
  hex_str = binascii.unhexlify(data)
  return hex_str

def init():
  #get bits
  file = getfile()
  fin = open(file, "rb")
  data = fin.read()
  data = str(data)
  data = bin(int.from_bytes(data.encode(), 'big'))
  data = data[2:]

  #get passkey
  key = getpass()

  return (int(key), int("1"+str(data)), file) # add 1 to beginning of data to avoid "SyntaxError: leading zeros in decimal integer literals are not permitted"

def encrypt():
  key, binary, file = init()
  num1 = key^2+key
  y = ((binary*key)*num1)

  f = open(file+"_encrypted", "w+")
  f.write(str(y))
  f.close()
  

def decrypt():
  #get bits
  fin = getfiledec()
  f = open(fin, "r")
  file = f.read()
  data = int(file)
  
  #get passkey
  key = int(getpassdec())

  # get num1
  num1 = key^2+key

  # decrypt text and remove the added one
  data = data//num1
  data = data//key
  data = str(data)[1:]
  data = "0b"+data

  # finally we convert it back to hex bytes
  data = int(data, 2)
  data = data.to_bytes((data.bit_length() + 7) // 8, 'big').decode()
  print(data)
  
  # then write to decrypted file
  f = open(fin+"_decrypted", "w+")
  f.write(data)
  f.close()


  

