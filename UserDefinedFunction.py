#Function With No Argument & No Return Value

def printLine():
    print("*"*60)

printLine()
print("Welcome To User Defined Function In Python.")
printLine()

#Function With Argument & No Return Value.

def sum(a,b):
    print("Sum : ",a+b)

printLine()
x=int(input("Enter Value : "))
y=int(input("Enter Value : "))
sum(x,y)
printLine()

#Function With Argument & Return Value.

def sub(a,b):
    return a-b

printLine()
x=int(input("Enter Value : "))
y=int(input("Enter Value : "))
#ans=sub(x,y)
print("Subtraction : ",sub(x,y))
printLine()
