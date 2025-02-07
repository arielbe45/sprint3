import os
import zipfile
import io


def folder_to_bytes(folder_path) -> bytes:
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


def bytes_to_folder(byte_data, output_folder):
    # Create a BytesIO object from the byte data
    zip_buffer = io.BytesIO(byte_data)

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Create "TheLeak" folder inside the output folder
    leak_folder = os.path.join(output_folder, "TheLeak")
    os.makedirs(leak_folder, exist_ok=True)

    # Open the zip file
    with zipfile.ZipFile(zip_buffer, 'r') as zip_ref:
        # Extract all contents to "TheLeak" folder
        zip_ref.extractall(leak_folder)

