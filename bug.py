def function_with_uncommon_error(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid input types")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    return result

# Example usage
result1 = function_with_uncommon_error(10, 2)
print(f"Result 1: {result1}")  # Output: Result 1: 5.0

result2 = function_with_uncommon_error(10, 0)
print(f"Result 2: {result2}")  # Output: Error: Division by zero
                                    #          Result 2: None

result3 = function_with_uncommon_error(10, "abc")
print(f"Result 3: {result3}")  # Output: Error: Invalid input types
                                    #          Result 3: None

result4 = function_with_uncommon_error(10, [1,2])
print(f"Result 4: {result4}") # Output: An unexpected error occurred: unsupported operand type(s) for /: 'int' and 'list'
                                    #          Result 4: None