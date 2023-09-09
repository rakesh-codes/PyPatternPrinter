num_lines =int(input("Ente the number of lines to be printed: "))

for i in range(1, num_lines +1):
    for j in range(1, num_lines +1):
        print(f"{(i) :3}", end="")
        print(f"{(j) :3}", end="")  
    print()