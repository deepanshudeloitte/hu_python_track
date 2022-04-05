st=1
n=5
for i in range(1,n+1):
    for j in range (1,n-i+1):
        print(" ",end="")
    for k in range(1,st+1):
        if i==1 or i==n or k==1 or k==st:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    st+=2