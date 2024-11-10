# Function to check if the person can vote
def can_vote(age):
    # If age is 18 or more, return True (eligible to vote)
    if age >= 18:
        return True
    else:
        return False

# Main function to take input and display result
def main():
    # Input the age of the person
    age = int(input("Enter your age: "))
    
    # Check if the person can vote and display the result
    if can_vote(age):
        print("You are eligible to vote!")
    else:
        print("You are not eligible to vote.")

# Call the main function
if __name__ == "__main__":
    main()
