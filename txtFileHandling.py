import os

# Mode x --> it will create file if not exists
#        --> it will throw exception if same file already exists


# Model w --> it will create file if not exists
#          --> 

# Mode r --> for reading content from  the file

try:
  # create file
  file= open("Techyardhi.txt",'w')
  print('File Created successfully')
  # write in write in file
  file.write("Hello Techyardhi \n")
  file.write("Welcome to Python programming world \n")
  file.write("Keep practicing for getting job on python programming Language \n")
  # close opened file
  file.close()
  # open file for content reading
  file= open("Techyardhi.txt",'r')
  contentinFile=file.read()
  print(contentinFile)
  #close file
  file.close()
 
  file= open("Techyardhi.txt",'r')
  contentinList=file.readlines()
  #print(contentinList[2]) 
  contentinList.insert(1,"Consistency is very important for succesing in career or life \n") 
  file.close()
   
  for eachline in contentinList:
    print(eachline)

  file.close()

  file= open("Techyardhi.txt",'w')
  for line in contentinList :
   file.write(line)
  file.close()

  os.remove("Techyardhi.txt")

except Exception as ex:
  print(f"Exception {ex}")
  


# Absolute Path : Complete path given to file creation
# Related Path : 