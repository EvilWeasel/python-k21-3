def bitwise_not():
  numlist = []
  num = 1
  while num < 10000:
    numlist.append(num)
    num*=2
  return numlist
    

    

numlist = bitwise_not()
for num in numlist:
  print(~num)