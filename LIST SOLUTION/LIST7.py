#create list of 5 value with file name and extension.Replace extension with ".c" with ".py" and print new list.

def changenamme(n):
    filechange=[]
    p=".c"
    for i in n:
        if p in i:
            b=i.replace(".c",".py")
            filechange.append(b)

        else:
            filechange.append(i)


    print(filechange)
  
filesname = ["program.c","stdio.c","sample.c","a.py","math.py","hpp.py"]
print(filesname)

