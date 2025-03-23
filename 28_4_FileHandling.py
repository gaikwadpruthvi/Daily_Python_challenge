#	Implement a function that safely opens files using with statements.

def safe_file_open():
    filename = input("Enter the filename: ")
    mode = input("Enter the mode (r for read, w for write, a for append): ").strip().lower()

    try:
        with open(filename, mode) as file:
            if mode == "r":
                content = file.read()
                print("File Content:\n", content)
            else:
                content = input("Enter text to write/append to the file: ")
                file.write(content + "\n")
                print("Content written successfully.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to access '{filename}'.")
    except IOError as e:
        print(f"IOError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
safe_file_open()
