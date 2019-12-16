#Text -> Number function, accepts all ascii input
def tonum( p ):
  pswd = []
  pswd[:0] = p
  result = ""
  print(pswd)
  for i in range(len(pswd)): 
    num = ord(pswd[i])
    result += str(num)
  return result
