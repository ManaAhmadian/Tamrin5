m=int(input("daryaft m:"))
n=int(input("daryaft n:"))
def safe_shatrangy(m,n):
    for i in range(m):
        for j in range(n):
            if (i+j)%2==0:
                print("#",end=" ")
            else:
                print("*",end=" ")
        print()
safe_shatrangy(m,n)
