num_lines = int(input("Enter the number of lines to be printed: "))
char = " * "

for i in range(1,num_lines+1): 
        print(f"{(i*char):4}", end=" ")
        print()