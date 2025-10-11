import csv,os

# x - creation of file if already not exists. it will trhow exception if same file already exists
# w - it will create a file if not exists. it will not if already exists

file = open('studentnames.csv',"w",newline="")
writer= csv.writer(file)

writer.writerow(["Name","Course","Qualification","Status"])


writer.writerow(['Satish',"AI/ML",'B.Tech',"Present"])
writer.writerow(['Anil',"ML",'B.Tech',"Present"])
writer.writerow(['Sai Ram',"Data Science",'M.Tech',"Present"])
writer.writerow(['Gopi Chand',"Full Stack Web",'B.Tech',"Present"])
writer.writerow(['Akash',"AI/ML",'B.Tech',"Present"])
writer.writerow(['Vinay',"AI/ML",'B.Tech',"Present"])
writer.writerow(['Swapna',"AI/ML",'B.Tech',"Present"])

file.close()

file= open("studentnames.csv","r")
reader= csv.reader(file)


#print(reader)
for row in reader:
    print(row)

file.close()


file= open("studentnames.csv","a",newline="")
writer=csv.writer(file)
writer.writerow(["Surya","DevOps","B.SC","Absent"])

file.close()

file= open("studentnames.csv","r")
reader= csv.reader(file)
rows= list(reader)
file.close()

#print(reader)
for row in rows:
    if row[0]== 'Satish':
        row[1]="Data Science"

file= open('studentnames.csv',"w",newline="")
writer=csv.writer(file)
writer.writerows(rows)

file.close()


file= open("studentnames.csv","r")
reader= csv.reader(file)


#print(reader)
for row in reader:
    print(row)

file.close()

#os.remove('studentnmes.csv')

if os.path.exists("studentnames.csv"):
    os.remove("studentnames.csv")
    print('file deleted successfully')
else:
    print('file not exists')

# Code Reusablity
# Code Readability
# Code maintanance
# Prper Commenting
# proper Naming Conventions


#JSON - JavacSript Object Notation