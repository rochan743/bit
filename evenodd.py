def isEvenOdd(n):
    if(n^1 == n+1):
        return True
    else:
        return False
    
n =int(input("Enter the number: "))

if isEvenOdd(n):
    print("Even") 
else:
    print("Odd")
       