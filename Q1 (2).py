# Function to calculate the factorial of a number
def factorial(n):
    # If the number is 0 or 1, return 1 as the factorial of both is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Initialize result to 1
        result = 1
        # Loop through all numbers from 1 to n and multiply them to find the factorial
        for i in range(1, n + 1):
            result *= i
        return result

# Main function to take input and display the result
def main():
    # Input from the user
    number = int(input("Enter a number to find its factorial: "))
    
    # Call the factorial function and store the result
    result = factorial(number)
    
    # Print the factorial
    print(f"The factorial of {number} is {result}")

# Call the main function to execute the program
if __name__ == "__main__":
    main()
