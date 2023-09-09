num_lines = int(input("Enter the number of lines to be printed: "))

for i in range(1, num_lines + 1):
    p = i
    q = num_lines - i + 1
    
    for j in range(1, num_lines + 1):
        if j % 2 == 0:
            print(f"{p :3}", end="")
        else:
            print(f"{q :3}", end="")
            
        q = q + num_lines
        p = p + num_lines
    print()
