single_line=input("enter 5 numbers in a single line ")
numbers_in_list=single_line.split(" ")
sum=0
for i in numbers_in_list:
    sum=sum+int(i)
    
print(f"The sum of the list of numbers is {sum}")
