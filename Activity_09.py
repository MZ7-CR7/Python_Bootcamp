import math
input_values=input("Enter the values of l & b & h in this given order")
list=input_values.split(" ")
L=int(list[0])
B=int(list[1])
H=int(list[-1])
k=(L**2 + B**2 + H**2)
vol=(B**2 * H**2)/math.sqrt(k)
print(f"{round(vol,3)} {k}")
