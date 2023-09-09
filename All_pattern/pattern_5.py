n=int(input("Ente the number of lines to be printed: "))

for i in range(1,n+1):
    for j in range(0, n):
        print(f"{n-j}" , end=" ")
    print()