#write a script to replace list's item with new value if found. Take value from user which you want to replace.

def change(n):
    m=[]
    b=int(input("Enter value you want to replace:"))
    c=int(input("Enter value you want to chaange with:"))
    for i in n:
        if b==i:
            m.append(c)
        else:
            m.append(i)

    print(m)

def createlist():
    a=[]
    b=int(input("How many numbers you want to enter in list:"))
    for i in range(b):
        c=int(input("Enter a number:"))
        a.append(c)

    change(a)

createlist()

