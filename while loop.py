"""n=int(input("enter value: "))
i=0
while i<n:
    i+=1
    print("answer",i)"""


#       IF STATEMENT IN WHILE LOOP
""""
n=int(input("enter value: "))
i=1
while i<=n:
    if i==5:
        print("print this before 5")
    print("answer",i)
    i+=1
"""
# BREAK in WHILE LOOP is used to terminate the statement which is in while loop
"""
n=int(input("enter value: "))
i=1
while i<=n:
    if i==5:
        print("print this before 5")
        break
    print("answer",i)
    i+=1
"""

# CONTINUE in WHILE LOOP is used to skip the statement and continue to the next statement
"""
n=int(input("enter value: "))
i=0
while i<n:
    i+=1    
    if i==4:
        continue
        print("print this before 4")  #here the continue statement skips this and continue to the next statement
        
    print("answer",i)

"""

#PASS in the WHILE loop to pass the statement if it olso unfinished
"""
n=int(input("enter value: "))
i=0
while i<n:
    i+=1 
    if i==4:
        pass #Here we use if the if command but didn't use the print statement but the code gets executed
    print("answer",i)

"""