num_lines = int(input("Enter the number of lines to be printed: "))

for i in range(1,num_lines+1):
    for j in range(1,num_lines+1):
        if j%2 ==1 :
            print(f"{0:3}", end="")
        else:
            print(f"{1:3}", end="")
    print()