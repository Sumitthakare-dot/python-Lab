# Function to print the multiplication table of a number
def multiplication_table(number):
    # Loop through numbers 1 to 10 and print the multiplication table
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Main function to take input and display the table
def main():
    # Input the number for which the table is needed
    number = int(input("Enter a number to get its multiplication table: "))
    
    # Call the function to print the multiplication table
    multiplication_table(number)

# Call the main function
if __name__ == "__main__":
    main()
