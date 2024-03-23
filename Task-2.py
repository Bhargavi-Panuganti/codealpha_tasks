import os
import shutil

def organize_files(source_directory, destination_directory):
    #mapping a file extensions to destination directories
    type_directories = {
        '.pdf': 'Documents',
        '.docx': 'Documents',
        '.jpg': 'Images',
        '.mp4': 'Videos',
        '.mp3': 'Audio',
        '.txt': 'Text',
        '.xlsx': 'Spreadsheets',
        '.png': 'Images',
        
    }

    # Ensure destination directories exist, create them if not
    for directory in set(type_directories.values()):
        os.makedirs(os.path.join(destination_directory, directory), exist_ok=True)

    # Iterate through files in the source directory
    for filename in os.listdir(source_directory):
        source_path = os.path.join(source_directory, filename)

        # Skip directories
        if os.path.isdir(source_path):
            continue

        # Determine file type based on extension
        extension = os.path.splitext(filename)[1].lower()

        # Get the destination directory for the file type
        destination_dir = os.path.join(destination_directory, type_directories.get(extension, 'Others'))

        # Move the file to the corresponding directory
        destination_path = os.path.join(destination_dir, filename)

        try:
            # Move the file to the corresponding directory
            shutil.move(source_path, destination_path)
            print(f"Moved {filename} to {destination_path}")
        except FileNotFoundError as e:
            print(f"Error: {e}. File not found.")
        except Exception as e:
            print(f"Error moving {filename}: {e}")


source_directory ="C:/Users/user/OneDrive/Documents/Desktop/source_dir"
destination_directory ="C:/Users/user/OneDrive/Documents/Desktop/destination"
organize_files(source_directory, destination_directory)
