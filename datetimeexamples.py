from datetime import datetime, timedelta,time,date
#while True :
# print(datetime.time,end="\t") 


rechargeDate= datetime.now();

expiryDate= rechargeDate + timedelta(days=28)



todayDate= date.today()
birthDate= date(2000,5,25)
personAge= todayDate.year - birthDate.year
print(todayDate.year - birthDate.year)



# Ternary operator : short form of If else

'''
         'value if True'  Condition   else 'value if false'

Staus = 'Major' if personAge > 21 else 'Minor'

'''
'''
Status= None

if personAge> 21:
    Status='Major'
else :
    Status='Minor'
'''














#print('Age', age);

'''
01-22-2025 

22-01-2025

January 22 2025
'''

#print(expiryDate)









'''
 end = \n  # new line
       \t  # tab space
       \r  # replace
       Default 
'''
#print(datetime.today())






