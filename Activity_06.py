actual_list=input("Enter the 5 numbers single line")
list=actual_list.split()
sliced_list=list[0:3]
print(f'sliced_list {sliced_list}')
list[0]=0
list[4]=0
print(f'replaced list-1={list}')
list=sliced_list
list[0]=0
list[2]=0
print(f'replaced_list_2 ={list}')
