import os

def rename_images(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Set a counter for generating unique names
    counter = 21

    # Loop through each file in the folder
    for file_name in files:
        # Check if the file is an image (you can add more image file extensions if needed)
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # Generate a new name for the image
            new_name = f"patan_{counter}.jpg"

            # Create the full paths for the old and new names
            old_path = os.path.join(folder_path, file_name)
            new_path = os.path.join(folder_path, new_name)

            # Rename the file
            os.rename(old_path, new_path)

            # Increment the counter for the next image
            counter += 1

if __name__ == "__main__":
    # Replace 'your_folder_path' with the path to your folder containing images
    folder_path = '/Users/nirajanpaudel17/Documents/new-patan'

    rename_images(folder_path)
