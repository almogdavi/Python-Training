#this is a def example from calss
print("111 its a  def train")


def calculate(x,y):
    if x != y:
        print(f"{x} is not equal {y}")
    if x == y:
        print(f"{x} is equal {y}")    

calculate(9,9)


print("222 now its a different def train")

def factorial(x):
    if x == 0 or x == 1:
        return 2
    else:
        return x * factorial(x-1)
    
number = 5
print(f"factorial of {number} is: {factorial(number)}")


print("333 now its a if elif else train")

x=9
y=9

if x > y:
    print(f"{x} is larger then {y}")
elif x < y:
    print(f"{y} is larger then {x}")
else:
    print(f"{x} and {y} is equal")





