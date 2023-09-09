num_lines = int(input("Enter the number of lines to be printed: "))

temp=1
for i in range(0,num_lines):
    
    for j in range(i+1):
        print(f"{temp :3}", end=" ")
        temp += 1
    print()