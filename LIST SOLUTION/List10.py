#write a script to check if the list contains three consicutive  common numbers in pthon using udf.

def consecutivecommon(n):
    count=0
    b=[]
    for i in range(len(n)-2):
        if n[i]==n[i+1] and n[i+1]==n[i+2]:
            b.append(n[i])
            count+=1

        if count>0:
            print(f"consecutive commn number in list {n} as follow:{b}")
        else:
            print("No consecutive number in list!!)

def takeinput():
    a=[]
    b=int(input("How many number you want to enter in list:"))
    for i in range(b):
        c=int(input("Enter a value:"))
        a.append(c)
    consecutivecommon(a)



