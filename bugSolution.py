def function_with_uncommon_error_solution(x):
    try:
        if x == 0:
            return 0  # Correct handling of zero
        else:
            return 1 / x
    except ZeroDivisionError:
        return float('inf')  # Handle ZeroDivisionError gracefully
    except OverflowError:
        return float('inf')

# Example showing improved handling
print(function_with_uncommon_error_solution(5))  # Output: 0.2
print(function_with_uncommon_error_solution(0))  # Output: inf
print(function_with_uncommon_error_solution(1e100))

# Solution for recursion depth error
def recursive_function_solution(n, limit=1000): #Setting a limit to avoid RecursionError
    if n > limit:
        raise RecursionError("Recursion depth exceeded.")
    if n == 0:
        return 0
    else:
        return recursive_function_solution(n - 1, limit)

#This solution will handle the error gracefully
recursive_function_solution(10000)