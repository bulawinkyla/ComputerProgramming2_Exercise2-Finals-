try:
    message = input("Enter a message: ")

    with open("notes.txt", "w") as file:
        file.write(message)

    print("\nContent of file:")
    with open("notes.txt", "r") as file:
        content = file.read()
        print(content)

    new_message = input("Enter a new message: ")

    with open("notes.txt", "a") as file:
        file.write("\n" + new_message)

    print("\nUpdated content of file:")
    with open("notes.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("The file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")