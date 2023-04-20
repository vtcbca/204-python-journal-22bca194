#write a list of menudriven

a=[]
q="y"
while q=="y" or q=="Y":


    print("\n1.Add items in list.\n2.print string with even character in length.\n3 replace odd character of string with indrex no.\n4.enter start and value and extract character from the string\n")
    c=int(input("Enter your choice!!"))

if c==1:

            a="y"
            while a1=="y" or a1=="Y":
              i=input("Enter a string you want to enter:") 
              a.append(i)
              a1=input("do you add more string press (y\Y)")

elif c==2:
           b=[]
           count=0
           for i in a:
            if(len(i)%2==0):
                  b.append(i)
                  count+=1
            if count>0:
               print(f"string with even character is {b}")
           else:
               print("string has no even character in it....")

elif c==3:
      
             t=[]
             for i in a:
               for j in range(0,len(i),2):
                 i[j]=j
               t.append(i)  
             print(t)

elif c==4:
            s=int(input("Enter start index:"))
            e=int(input("Enter end index:"))
            res=" ".join([sub for sub in a])[s:e]
            print(f"your string is {res}")

else:
          print("Enter a valid choice!")


         q=input("Do you want to continue:(y/Y):")
