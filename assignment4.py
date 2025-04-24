def read_and_modify_file():
    try:
        # Ask user for the filename to read
        filename = input("Enter the name of the file to read: ")

        # Try to open and read the file
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the content (for example, make all text uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content has been written to '{new_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except IOError:
        print("❌ Error: Could not read the file.")

# Run the function
read_and_modify_file()
