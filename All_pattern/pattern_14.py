num_lines = int(input("Enter the number of lines to be printed: "))

for i in range(1, num_lines + 1):
    q = num_lines - i + 1
    for j in range(1, num_lines + 1):
            print(f"{q :3}", end="") 
            q = q + num_lines
    print()
