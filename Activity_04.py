a=int(input("enter the first number to add:"))
b=int(input("enter the second number to add:"))
z=a+b
#c script method
print("The sum of \n%d + %d = %d \n"%(a,b,z))
#end method
print(a,end=" + ")
print(b,end=" =")
print("",z)
#.format method
print("{0} + {1} = {2}".format(a,b,z))
#f-string method
print(f"The sum of\n{a} + {b} = {z}")
