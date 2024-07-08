import os
import zipfile
import io

def main():
    print("hello")


if __name__ == '__main__':
    main()



def folder_to_bytes(folder_path):
    # Create a BytesIO object to store the zip file
    zip_buffer = io.BytesIO()

    # Create a ZipFile object
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        # Walk through the folder
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Calculate the archive name (path relative to the folder)
                archive_name = os.path.relpath(file_path, folder_path)
                # Add the file to the zip
                zip_file.write(file_path, archive_name)

    # Get the bytes from the BytesIO object
    return zip_buffer.getvalue()


# Usage
folder_path = '/path/to/your/folder'
folder_bytes = folder_to_bytes(folder_path)

# Now folder_bytes contains the folder as bytes