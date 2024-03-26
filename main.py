# table_printer.py

a = int(input("Enter the number you want to print the table of : "))
b = int(input("Enter the number you want to print the table upto : "))
for i in range(b+1):
    print(f'{a} X {i} = {a*i}')
