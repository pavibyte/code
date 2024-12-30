from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def mutiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+": add,
              "-": subtract,
              "*": mutiply,
              "/": divide,
              }
def function_1():
    first_number = int(input("type the first number: "))
    def function_2(first_number):
        print("+\n-\n*\n/\n")
        operation_chosen = input("pic an operation: ")
        second_number = int(input("type the next number: "))
        if operation_chosen == "+":
            sol = add(first_number, second_number)

        elif operation_chosen == "-":
            sol = subtract(first_number, second_number)

        elif operation_chosen == "*":
            sol = mutiply(first_number, second_number)

        else:
            sol = divide(first_number, second_number)
        print(f"{first_number} {operation_chosen} {second_number} = {sol}")

        continue_or_new = input(f"type 'y' to continue with {sol} or type 'n' to start a new calculation: ")
        if continue_or_new == "y":
            first_number = sol
            function_2(sol)
        else:
            print("\n" * 20)
            function_1()
    function_2(first_number)
function_1()