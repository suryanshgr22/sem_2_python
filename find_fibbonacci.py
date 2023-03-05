n = int(input("Enter Number : "))
if n == 0:
    print("It is an fibbonacci No.")
    quit()

t = 0
n1 = 0
n2 = 1
while(t<n):
    t = n1 + n2
    n1 = n2
    n2 = t
    if(n==t):
        print("It is an fibbonacci No.")
        quit()
    
print("It is not an fibbonacci No.")
    
