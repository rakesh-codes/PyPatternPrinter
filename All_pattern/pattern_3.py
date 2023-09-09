n=int(input("Ente the number of lines to be printed: "))

for i in range(1,n+1):
    j=0
    for j in range(0, n+1):
        print(f"{j+1}", end=" ")
    print()