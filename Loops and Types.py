#To REPEAT something in the exact same way:
#1. For Loop
#2. While Loop
#3. While True
#4. Nested Loop

###1. For Loop : repeating something in a given RANGE ::+1 is added to ending point.#
#For (Variable) in range (1,6): print (Variable):: ##1,2,3,4,5,6
#For (Variable) in range (1,6): print ("Hello World") :: ##Hello World 5times
#For (Variable) in range (1,6): print (Variable):: ##1,3,5

#for i in range (1,6):
#    print("hello world") ##hello world 5 times

#for i in range (1,6,2):
#    print(i)             ##1,3,5

#n=7
#for i in range (1,11):
#    print(n,"X",i,"=",n*i)  ##7x1=7, 7x2=14, till 10)

#n=9
#for i in range (1,10):
#    print(n,"X",i,"=",n*i)  ##8x1=8, 8x2=16, till 9)

#n= int (input("enter a number here: "))
#for i in range (1,11):
#    print(n,"x",i,"=",n*i)   ##enter a number here:12,##12x1=12, till 12x10=120##

#n= int(input("enter a number here: "))
#for i in range (1,51,3):
#    print(n,"x",i,"=",n*i)   ##enter a number here:12,##12x1=12,12x4=48, till 12x50=600##


###2. While Loop :It executes till given condition is TRUE.The INCREMENT is Done inside the LOOP.
#n=2
#while n<=10:
#    print(n)
#    n+=2                    ##2,4,6,8,10

n=1
a=int(input("enter a number here: "))

while n<=10:
    print(a,"x",n,"=",n*a)
    n+=2
while n<=10:
    print(a,"x",n,"=",n*a)
    n+=2

