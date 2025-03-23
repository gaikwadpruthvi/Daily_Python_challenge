#	Implement a function that handles KeyError while accessing dictionary keys.

def manage_dictionary(data_dict):
    try:
        key = input("Enter the key: ")
        
        if key in data_dict:
            print(f"Current value: {data_dict[key]}")
            choice = input("Do you want to update this key's value? (yes/no): ").strip().lower()
            if choice == "yes":
                new_value = input(f"Enter new value for '{key}': ")
                data_dict[key] = new_value
                print(f"Updated dictionary: {data_dict}")
            else:
                print(f"Value remains unchanged: {data_dict[key]}")
        else:
            print(f"KeyError: The key '{key}' does not exist.")
            choice = input("Do you want to add this key? (yes/no): ").strip().lower()
            if choice == "yes":
                new_value = input(f"Enter value for new key '{key}': ")
                data_dict[key] = new_value
                print(f"Updated dictionary: {data_dict}")
            else:
                print("No changes made to the dictionary.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
sample_dict = {"name": "Alice", "age": 25, "city": "Birmingham"}

manage_dictionary(sample_dict)
