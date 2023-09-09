num_lines = int(input("Enter the number of lines to be printed: "))
temp=0
for i in range(1,num_lines+1):
    
    for j in range(i):
        print(f"{i*i+temp :3}", end=" ")
        temp -= 1
    print()