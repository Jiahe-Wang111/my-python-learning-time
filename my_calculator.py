# TODO: Write out the other 4 functions, add, subtract, multiply, and divide.
def add(a, b):
    return  a + b
def subtract(a, b):
    return  a - b

def multiply(a, b):
    return  a * b

def divide(a, b):
    return  a / b

# TODO: Add these 4 functions into a dictionary as a value. Keys = "+", "-", "*", "/".
dictionary = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

# print(dictionary)

def calculator():
    """A simple command-line calculator."""
    print(r'''_____________________
|  _________________  |
| |              /  | |
| |       /\    /   | |
| |  /\  /  \  /    | |
| | /  \/    \/     | |
| |/             JO | |
| |_________________| |
|  __ __ __ __ __ __  |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
''')

    try:
        first_number = float(input("What's the first number? "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        calculator()
        return
        # 或重新提示输入 # 使用float而不是int是为了结果不局限于整数
    n = True

    while n:
        for symbol in dictionary:
            print(symbol)
        operation = input("Pick an operation: ")
        next_number = float(input("What's the next number? "))
        result = dictionary[operation](first_number, next_number)
        print(f"{first_number} {operation} {next_number} = {result}")

        chooser = input(f"Type 'y' to continue with {result},"
                        f"or type 'n' to start a new calculation: ,"
                        f"or type 's' to stop this calculator.").lower()

        if chooser == "y":
            first_number = result  # 用上一次的结果继续
        elif chooser == "n":
            print("\n" * 20)    # 换页符
            calculator()
            break
        elif chooser == "s":
            print("Calculator closed. Goodbye!")
            n = False

calculator()
