def main():
    print("Enter the value of first number")
    a=input_number()
    print("Enter the value of second number")
    b=input_number()
    summation=add(a,b)
    display(a,b,summation)

def input_number():
    return int(input())
def add(a,b):
    return a+b
def display(a,b,summation):
    print(f"The sum of {a}+{b}={a+b}")

main()
   
