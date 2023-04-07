#write a script to create dictionary from list which contain student id,name and percentage.

n=int(input("Enter number of student details you want to add:"))

i=[]
mydict={}
for i in range(0,n):

     a=int(input("Enter id number of student:"))
     b=int(input("Enter name of student:"))
     c=int(input("Enter percentage of student:"))

l.append([b,c])

mydict[a]=l[i]
for i in mydict:
         if mydict[i][1]>=75:
             print(mydict[i])
             
