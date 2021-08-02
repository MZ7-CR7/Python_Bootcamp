actual_list=input("Enter the 5 numbers single line")
list=actual_list.split()
sliced_list=list[0:3]
print(f'sliced_list {sliced_list}')
list[0]=0
list[4]=0
replaced_list1=list[::]
print(f'replaced_list1={replaced_list1}')
list=sliced_list
list[0]=0
list[2]=0
replaced_list_2=list
print(f'replaced_list_2 ={replaced_list_2}')
