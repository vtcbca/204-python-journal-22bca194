#WAS to create  udf input() to take input string and call strsymmetric() by inputted string.
#strsymettric() check string is symmetric or not.A string is said to be symmetrical if both the halves of the string are the same.
#Example:
#Enter string : khokho
#string is symmetrical.



def symmetric(n):
    half=(len(n)//2)
    first=n[:half]
    second=n[half:]
    if first==second:
        print(f"string {n} is symmetric!!!")
    else:
        print(f"string {n} is not symmetric!!!")

def input1():
     a=input("Enter a string:")
     symmetric(a)

input()     
