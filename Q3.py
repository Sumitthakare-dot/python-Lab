# Function to calculate sum of digits using a while loop
def sum_of_digits(num):
    # Input validation to check if the number is valid
    if num < 0:
        num = abs(num)  # Convert negative number to positive if required

    digit_sum = 0
    
    # Loop to calculate the sum of digits
    while num > 0:
        digit_sum += num % 10  # Add the last digit
        num //= 10  # Remove the last digit by integer division
    
    return digit_sum

# Taking user input with validation
try:
    num = int(input("Enter a number to calculate the sum of its digits: "))
    print(f"The sum of digits of {num} is: {sum_of_digits(num)}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
