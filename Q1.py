# Function to calculate factorial using a while loop
def factorial(num):
    # Input validation to check if the number is negative
    if num < 0:
        return "Factorial is not defined for negative numbers"
    
    # Initialize result to 1 (factorial of 0 is 1)
    result = 1
    
    # Calculate the factorial using a while loop
    while num > 1:
        result *= num  # Multiply result by the current num
        num -= 1  # Decrement num to move towards 1
    
    return result

# Taking user input with validation for an integer
try:
    num = int(input("Enter a number to calculate its factorial: "))
    print(f"The factorial of {num} is: {factorial(num)}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
