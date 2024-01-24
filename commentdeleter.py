# Written by ByteMaestr0
# Mainly used to delete comments from program(lines that start with: #, //, /*;)
# Importing the os library to work with file paths
import os
# Importing the platform library to detect the working system
import platform

# Make the function that detects the system shorter, so it's easier to call

sys = platform.system()

if sys == "Windows":
    def clear():
        os.system("cls")
elif sys == "Linux" or sys == "Darwin":
    def clear():
        os.system("clear")
else:
    print("Your system isn't recognized. Program might not run as intended.")
# Function to extract the filename from a given file path
def extract_file_name(file_path):
    # Use os.path.basename to get the filename from the path
    file_name = os.path.basename(file_path)
    return file_name

# Function to find and delete lines containing specified strings in a file
def find_and_delete_strings(file_path, strings_to_find, search_at_start=True):
    # Calling the function to extract the filename from the file path
    file_name = extract_file_name(file_path)

    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read all lines from the file into a list
            lines = file.readlines()

        # Find lines containing specified strings
        matching_lines = []
        for i, line in enumerate(lines):
            # Check if the specified strings are at the start of the line
            if search_at_start and any(line.strip().startswith(string) for string in strings_to_find):
                matching_lines.append(i + 1)
            # Check if the specified strings are anywhere in the line
            elif not search_at_start and any(string in line for string in strings_to_find):
                matching_lines.append(i + 1)

        # If no matching lines are found, print a message and return
        if not matching_lines:
            clear()
            print("No matching lines found.")
            return

        # Display lines containing the specified strings
        clear()
        print("Lines containing the specified strings:")
        for i, line_number in enumerate(matching_lines):
            print(f"{line_number}) {lines[line_number - 1].rstrip()}")

        # Get user input for lines to delete
        delete_input = input(f"Which line(s) to delete? (e.g., x-y or x): ")

        # Parse user input to determine lines to delete
        if '-' in delete_input:
            start, end = map(int, delete_input.split('-'))
            lines_to_delete = set(range(start, end + 1)) & set(matching_lines)
        else:
            line_to_delete = int(delete_input)
            lines_to_delete = {line_to_delete}

        # Create a list of updated lines (excluding the lines to delete)
        updated_lines = [line for i, line in enumerate(lines) if i + 1 not in lines_to_delete]

        # Display success message for line deletion
        if len(lines_to_delete) == 1:
            print(f"Line {list(lines_to_delete)[0]} deleted successfully.")
        else:
            print(f"Lines deleted successfully.")

        # Get user input for output file option
        clear()
        print("Do you want to save the updated file as '" + file_name + "' or '" + file_name + ".updated'? (Default is '" + file_path + "')")
        print(file_name + " = 1")
        print(file_name + ".updated = 2")

        output_option = input("").lower()

        # Determine the output file path based on user input
        if output_option == "2":
            updated_file_path = file_path + ".updated"
        elif output_option == "1":
            updated_file_path = file_path
        else:
            print("Saving as '" + file_name + "' by default.")
            updated_file_path = file_path
        clear()

        # Write the updated lines to the output file
        with open(updated_file_path, 'w') as file:
            file.writelines(updated_lines)

        print(f"Updated file saved to {updated_file_path}")

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main program
if __name__ == "__main__":
    # Make the screen cleaner
    clear()
    # Get user input for file location, strings to find, and search at start option
    file_path = input("Enter the file location (e.g., /x/y/z): ")
    clear()
    strings_to_find = input("Enter strings to find (e.g., 'example', 'test'): ").split(',')
    clear()
    search_at_start_input = input("Do you want to search for the given strings only at the start of the line? (leave blank for no): ")
    search_at_start = search_at_start_input.lower() != 'n' if search_at_start_input else False
    clear()

    # Call the function to find and delete lines
    
    find_and_delete_strings(file_path, strings_to_find, search_at_start)
