n = int(input("Enter terms : "))
if n == 1:
    print("0")
    quit()
elif n == 0:
    quit()
else:
    print("0 , 1",end='')
t = 0
n1 = 0
n2 = 1
for i in range(1,n-1):
    t = n1 + n2
    n1 = n2
    n2 = t
    print(", "+str(t),end='')

    