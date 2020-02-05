frequency_dict={}
string=input("Enter String:")
string=list(string)
print(string)
for x in string:
  if x in frequency_dict:
    frequency_dict[x]=frequency_dict[x]+1
  else:
      frequency_dict[x]=1
print(frequency_dict)