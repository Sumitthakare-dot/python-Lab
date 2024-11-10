# Function to print Fibonacci series up to n terms using a while loop
def fibonacci(n):
    # Input validation to check if n is a positive integer
    if n <= 0:
        return "Please enter a positive integer for the number of terms."

    # First two terms of the Fibonacci series
    a, b = 0, 1
    count = 0

    # Loop to print Fibonacci series up to n terms
    while count < n:
        print(a, end=" ")  # Print the current term
        a, b = b, a + b  # Update the terms (a becomes b, b becomes a + b)
        count += 1  # Increment the count of terms printed

# Taking user input with validation
try:
    n = int(input("Enter the number of terms for Fibonacci series: "))
    print("Fibonacci series up to", n, "terms:")
    fibonacci(n)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
