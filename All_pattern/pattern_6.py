n=int(input("Ente the number of lines to be printed: "))

for i in range(0,n):
    for j in range(1, n+1):
        print(f"{i*n+j:2}", end="  ")
    print()