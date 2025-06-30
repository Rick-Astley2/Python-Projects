import math

def main():
    try:
        x, y, z = input("Type out a math problem: ").split() # if you would like to find the root of a number,    
                                                         # type out the first number, then press "opt + v" and type 0 for the second number
        x = int(x)
        z = int(z)
        calculate(x, y, z)
    except ValueError:
        print("Input two numbers and an operation.")
        
    

def calculate(x, y, z):       
    if not number_check(x, z):  
        print("Please input valid numbers.")
        return  # Stops execution if inputs are invalid

    if y == "+":
        print(x + z)
    elif y == "-":
        print(x - z)
    elif y == "*":
        print(x * z)
    elif y == "/":
        if z == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(x / z)
    elif y == "^":
        print(x ** z)
    elif y == "√":
        if x < 0:
            print("Error: Cannot take the square root of a negative number.")
        else:
            print(math.sqrt(x))
    else:
        print("Error: Unsupported operation.")


                       
def number_check(x, z):
    return isinstance(x, (int, float)) and isinstance(z, (int, float))

        
if __name__ == "__main__":
    main()
