def char_occurance(string):
  hash={}
  for i in string:
    if i in hash:
      hash[i]+=1
    else:
      hash[i]=1
  return hash

print(char_occurance("mnun"))
