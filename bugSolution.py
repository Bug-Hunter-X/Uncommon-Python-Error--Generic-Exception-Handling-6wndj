def function_with_improved_error_handling(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Inputs must be numbers")
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        result = a / b
        return result
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None
    except TypeError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example Usage
result1 = function_with_improved_error_handling(10, 2)
print(f"Result 1: {result1}")  # Output: Result 1: 5.0

result2 = function_with_improved_error_handling(10, 0)
print(f"Result 2: {result2}")  # Output: Error: Division by zero
                                    #          Result 2: None

result3 = function_with_improved_error_handling(10, "abc")
print(f"Result 3: {result3}")  # Output: Error: Inputs must be numbers
                                     #          Result 3: None

result4 = function_with_improved_error_handling(10, [1,2])
print(f"Result 4: {result4}") # Output: Error: Inputs must be numbers
                                    #          Result 4: None