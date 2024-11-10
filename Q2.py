# Function to count digits using a while loop
def count_digits(num):
    # Input validation to check if the number is valid
    if num < 0:
        num = abs(num)  # Convert to positive if negative (optional, depends on requirement)

    # Initialize the count to 0
    digit_count = 0

    # Loop to count digits
    while num > 0:
        num //= 10  # Integer division to remove the last digit
        digit_count += 1  # Increment count
    
    return digit_count

# Taking user input with validation
try:
    num = int(input("Enter a number to count its digits: "))
    print(f"The number of digits in {num} is: {count_digits(num)}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
