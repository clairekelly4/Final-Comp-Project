import os

current_name = "finalproject.py"
new_name = "main.py"

try:
    os.rename(current_name, new_name)
    # or
    # os.replace(current_name, new_name)
    print(f"File renamed successfully from {current_name} to {new_name}")
except FileNotFoundError:
    print(f"Error: File {current_name} not found.")
except FileExistsError:
    print(f"Error: File {new_name} already exists.")
except Exception as e:
    print(f"An error occurred: {e}")