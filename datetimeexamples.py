from datetime import datetime, timedelta,time,date
#while True :
# print(datetime.time,end="\t") 


rechargeDate= datetime.now()

expiryDate= rechargeDate + timedelta(days=28)



todayDate= date.today()
birthDate= date(2000,5,25)
personAge= todayDate.year - birthDate.year
#print(todayDate.year - birthDate.year)



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



#Conversion of DateTime or Date to String




current_date= datetime.now()

#print(current_date)

#print(type(current_date))


string_dateTime= current_date.strftime("%d - %b - %Y")

#print(string_dateTime)


'''
%Y   - 2025
%y   - 25
%m   - (1-12)
%b   - oct
%B   - October
%H   - Hours (24 hours time)
%I   - Hours (12 hours time)
%M   - Minutes
%S   - Seconds
%p - AM/PM
%A - Week Name
'''


#Conversion of String or Date to 




date_string ="2000-10-20"

date_obj = datetime.strptime(date_string,"%Y-%m-%d")

try:
  if date_obj.month == datetime.today().month and date_obj.strftime("%")== datetime.today().strftime("%d") : 
    #end 
    print('Send Birth Day Notification')
    print('test')
except:
    print('Some Went wrong, Please Contact Administrator')



 #datetime.today().strftime("%A") =="hursday"  
   


#01-01-2000







#print(date_obj)

#print(type(date_obj))

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






