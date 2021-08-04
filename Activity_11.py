def main():
    print(f"Enter the value of a=")
    a=input_number()
    print(f"Enter the value of b=")
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
   
