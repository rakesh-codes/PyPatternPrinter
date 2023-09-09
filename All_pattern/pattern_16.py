num_lines =int(input("Ente the number of lines to be printed: "))

for i in range(1, num_lines +1):
    for j in range(0, num_lines ):
        print(f"{(i+j) :3}", end="")
    print()