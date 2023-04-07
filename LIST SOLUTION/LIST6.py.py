#was to create list using createlist().count and print even and odd number in the list using UDF even odd.

def evenodd(n):
    even,odd=[],[]
    count1,count2=0,0
    for i in n:
        if i%2==0:
            even.append(i)
            count1+=1
        else:
            odd.append(i)
            count2+=2

    print(f"The even number are {count1} and number:")
    printlist(even)

    print(f"The odd numbers are {count2} and numbers:")
    printlist(odd)


def printlist(b):
    for i in b:
        print(i)


def createlist():
    a=[]
    b=int(input("How many number you want to enter in list:"))
    for i in range(b):
        c=int(input("Enter a number:"))
        a.append(c)
    evenodd(a)


createlist()    
