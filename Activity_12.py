def largest(x, y, z):
    if x > y and x > z:
        return x
    elif y > z and y > x:
        return y
    elif z > x and z > y :
        return z

numbers_list=input("Enter the values in a list")
number=numbers_list.split(" ")

x = int(number[0])
y = int(number[1])
z = int(number[-1])

result = largest(x, y, z)

if (result!=None):
    print(f"{result} is the greatest among {x},{y},{z}:")
else:
    print("All are equal")
