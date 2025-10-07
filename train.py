#this is a def example from calss

def calculate(x,y):
    if x != y:
        print(f"{x} is not equal {y}")
    if x == y:
        print(f"{x} is equal {y}")    

calculate(9,9)

print("now its a different def train")

def factorial(x):
    if x == 0 or x == 1:
        return 2
    else:
        return x * factorial(x-1)
    

number = 5
print(f"factorial of {number} is: {factorial(number)}")

