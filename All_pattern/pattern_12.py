num_lines =int(input("Ente the number of lines to be printed: "))

for i in range(1, num_lines +1):
    print(f"{(i) :3}", end="")
    for j in range(1, num_lines ):
        print(f"{(num_lines*j)+1 :3}", end="")  
    print()