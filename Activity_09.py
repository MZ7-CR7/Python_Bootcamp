import math
input_values=input("Enter the values of l & b & h in this given order")
list=input_values.split(" ")
L=float(list[0])
B=float(list[1])
H=float(list[-1])
k=(L**2 + B**2 + H**2)
vol=(B**2 * H**2)/math.sqrt(k)
r=((3*vol)/(4*math.pi))**(1/3)
print(f"volume of tromboloid= {vol:.3f} \nvalue of K={k}\n radius of sphere ={r:.3f}")
 
  
