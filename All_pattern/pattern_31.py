num_lines = int(input("Enter the number of lines to be printed: "))


for i in range(0,num_lines):
    for j in range(0,num_lines):
      print(f"{chr(60+num_lines+j+i):3}", end="")
    print()