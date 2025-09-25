#syntax of while loop

'''
while condition :
    statement 1
    stetement 2 
'''
'''
correct_pin = 1234  
entered_pin = int(input("enter your PIN : "))
count =1;
while entered_pin != correct_pin :
  if count <3 :
   entered_pin = int(input("enter valid PIN : "))
   count +=1 
  else :
    print('your account is blocked')
    break
'''  

connected=False
attempts =0

while not connected and attempts < 5 :
  print("trying to Connect wi fi")
  attempts+=1
  if attempts==4 :
     connected=True


if connected :
  print('Connected to Wifi')
else :
  print('not connected to wifi')


downloadProgress =0
internetConnection= True
while downloadProgress <=50 : 
  downloadProgress+=1
  if downloadProgress % 2==0 :
     continue
  print(f"Download load in progress: {downloadProgress}" )
  if downloadProgress == 40:
    break
else :
    print('loop successfuuly ended')


 # else in loop : when loop completes with out break statement execution
 # continue : it will skip the statements execution and keep iterating loop
 # break : it will break the loop and exits immidaitely
  

  


  

     
 




 
  


 
 
