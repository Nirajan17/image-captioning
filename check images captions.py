import os
import pandas as pd

def check_images(csv_file, image_folder):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Initialize a counter for missing images
    missing_count = 0

    # Iterate through each row in the DataFrame
    for index, row in df.iterrows():
        # Get the image name from the "Image_name" column
        image_name = row['Image_name']

        # Search for the image file in the image folder
        image_files = [f for f in os.listdir(image_folder) if image_name in f]

        # Check if at least one matching image file is found
        if not image_files:
            print(f"Image not found for row {index + 1}: {image_name}")
            missing_count += 1
        else:
            # You can print the found image files if needed
            # print(f"Found image for row {index + 1}: {image_files}")
            pass

    # Print the total count of missing images
    print(f"Total missing images: {missing_count}")

if __name__ == "__main__":
    # Replace 'your_csv_file.csv' with the name of your CSV file
    csv_file_name = '/Users/nirajanpaudel17/Downloads/stanford_cultural_nepalis.csv'
    
    # Replace 'your_image_folder' with the path to your image folder
    image_folder_path = '/Users/nirajanpaudel17/Downloads/stanford_images'

    check_images(csv_file_name, image_folder_path)
