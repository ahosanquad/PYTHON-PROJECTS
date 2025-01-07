import os
import shutil

def list_files(directory):
    print(f"\nFiles in {directory}:")
    for filename in os.listdir(directory):
        print(filename)

def delete_file(filepath):
    try:
        os.remove(filepath)
        print(f"{filepath} deleted successfully.")
    except FileNotFoundError:
        print("File not found.")

def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        print(f"File copied from {source} to {destination}.")
    except FileNotFoundError:
        print("Source file not found.")
    except Exception as e:
        print(f"Error copying file: {e}")

def move_file(source, destination):
    try:
        shutil.move(source, destination)
        print(f"File moved from {source} to {destination}.")
    except FileNotFoundError:
        print("Source file not found.")
    except Exception as e:
        print(f"Error moving file: {e}")

def rename_file(filepath, new_name):
    try:
        new_filepath = os.path.join(os.path.dirname(filepath), new_name)
        os.rename(filepath, new_filepath)
        print(f"File renamed to {new_name}.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error renaming file: {e}")

def search_file(directory, filename):
    found = False
    for root, dirs, files in os.walk(directory):
        if filename in files:
            print(f"Found {filename} in {root}")
            found = True
    if not found:
        print(f"{filename} not found in {directory}.")

def file_manager():
    while True:
        print("\nSimple File Manager")
        print("1. List files in a directory")
        print("2. Delete a file")
        print("3. Copy a file")
        print("4. Move a file")
        print("5. Rename a file")
        print("6. Search for a file")
        print("7. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5/6/7): ")
        
        if choice == "1":
            directory = input("Enter the directory path: ")
            if os.path.isdir(directory):
                list_files(directory)
            else:
                print("Invalid directory.")
        
        elif choice == "2":
            filepath = input("Enter the file path to delete: ")
            if os.path.isfile(filepath):
                delete_file(filepath)
            else:
                print("File not found.")
        
        elif choice == "3":
            source = input("Enter the source file path: ")
            destination = input("Enter the destination file path: ")
            if os.path.isfile(source):
                copy_file(source, destination)
            else:
                print("Source file not found.")
        
        elif choice == "4":
            source = input("Enter the source file path to move: ")
            destination = input("Enter the destination file path: ")
            if os.path.isfile(source):
                move_file(source, destination)
            else:
                print("Source file not found.")
        
        elif choice == "5":
            filepath = input("Enter the file path to rename: ")
            new_name = input("Enter the new file name: ")
            if os.path.isfile(filepath):
                rename_file(filepath, new_name)
            else:
                print("File not found.")
        
        elif choice == "6":
            directory = input("Enter the directory to search in: ")
            filename = input("Enter the filename to search for: ")
            if os.path.isdir(directory):
                search_file(directory, filename)
            else:
                print("Invalid directory.")
        
        elif choice == "7":
            print("Exiting File Manager. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    file_manager()