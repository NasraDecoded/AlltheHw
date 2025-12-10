
# for loops
def make_operation(operator, arguments):
    
    if operator == "sum":
        result = 0
        for a in arguments:
            result += a

    elif operator == "mul":
        result = 1
        for b in arguments:
            result *= b
    elif operator == "sub":
        result = arguments[0]
        for c in arguments[1:]:
            result -= c
    return result

numbers = [7, 7, 2]

print(42 == make_operation("mul", [7, 6]))
print(16 == make_operation("sum", numbers))
print(30 == make_operation("sub", [5, 5, -10, -20]))