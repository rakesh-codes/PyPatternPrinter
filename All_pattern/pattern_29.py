num_lines = int(input("Enter the number of lines to be printed: "))


for i in range(1,num_lines+1):
    for j in range(1,num_lines+1):
      print(f"{chr(65+num_lines-j):3}", end="")
    print()