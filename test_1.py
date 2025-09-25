number= input("Enter Number: ")
total=0
for digit in number :
  print(digit,len(number))
  print(int(digit)**len(number))
  total += int(digit)**len(number)



if int(number)==total :
  print('Armstrong')
else :
  print("not")