# Function to find the maximum of two numbers
def find_max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

# Main function to take user input and display the result
def main():
    # Input two numbers
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    
    # Call the function and display the maximum number
    print(f"The maximum number is: {find_max(number1, number2)}")

# Call the main function
if __name__ == "__main__":
    main()
