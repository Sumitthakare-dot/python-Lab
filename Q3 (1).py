def check_item_in_list(item, item_list):
    # Traverse the list to check if the item is present
    if item in item_list:  # The 'in' operator checks if the item is in the list
        return True
    else:
        return False

# Example list
items = [1, 2, 3, 4, 5]

# Input from user
item_to_check = int(input("Enter the item to check if it's present in the list: "))

# Call the function and display the result
if check_item_in_list(item_to_check, items):
    print(f"The item {item_to_check} is present in the list.")
else:
    print(f"The item {item_to_check} is NOT present in the list.")
