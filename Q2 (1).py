def factorial(n):
    # Initialize result to 1 (since the factorial of 0 or 1 is 1)
    result = 1
    
    # Loop from 1 to n to calculate factorial
    for i in range(1, n + 1):
        result *= i  # Multiply the result by i in each iteration
    
    return result  # Return the calculated factorial

# Get user input
num = int(input("Enter a number to find its factorial: "))

# Call the factorial function and display the result
print(f"The factorial of {num} is {factorial(num)}")
