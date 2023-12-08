import os
import pandas as pd
from sklearn.model_selection import train_test_split
import shutil

def split_images_and_captions(caption_csv, image_folder, output_folder):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(caption_csv)

    # Split the data into training, validation, and test sets
    train_df, test_val_df = train_test_split(df, test_size=0.2, random_state=42)
    val_df, test_df = train_test_split(test_val_df, test_size=0.5, random_state=42)

    # Create folders for train, val, and test sets
    train_folder = os.path.join(output_folder, 'train')
    val_folder = os.path.join(output_folder, 'val')
    test_folder = os.path.join(output_folder, 'test')

    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(val_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)

    # Initialize counters for missing images
    missing_train_count = 0
    missing_val_count = 0
    missing_test_count = 0

    # Copy images to respective folders and update the DataFrame
    for split, split_df, split_folder, missing_count in [
        ('train', train_df, train_folder, 'missing_train_count'),
        ('val', val_df, val_folder, 'missing_val_count'),
        ('test', test_df, test_folder, 'missing_test_count')
    ]:
        for index, row in split_df.iterrows():
            image_name = row['Image_name']
            # Include the file extension in the image path
            image_path_src = os.path.join(image_folder, f"{image_name}.jpg")
            image_path_dest = os.path.join(split_folder, f"{image_name}.jpg")

            # Find the corresponding row in the DataFrame
            caption_row = df[df['Image_name'] == image_name]

            if not caption_row.empty:
                # Copy the image to the corresponding folder using shutil
                shutil.copy(image_path_src, image_path_dest)

                # Update the DataFrame with split information
                df.loc[df['Image_name'] == image_name, f'{split}_set'] = True
                df.loc[df['Image_name'] != image_name, f'{split}_set'] = False
            else:
                # Increment the missing count for the corresponding set
                if split == 'train':
                    missing_train_count += 1
                elif split == 'val':
                    missing_val_count += 1
                elif split == 'test':
                    missing_test_count += 1

    # Set values for 'train_set', 'val_set', and 'test_set' columns
    df['train_set'] = df['Image_name'].isin(train_df['Image_name'])
    df['val_set'] = df['Image_name'].isin(val_df['Image_name'])
    df['test_set'] = df['Image_name'].isin(test_df['Image_name'])

    # Save the updated DataFrame to a new CSV file (excluding rows with missing images)
    output_csv = os.path.join(output_folder, 'captions_with_splits.csv')
    df = df.dropna(subset=['train_set', 'val_set', 'test_set'])
    df.to_csv(output_csv, index=False)

    # Print count information
    print(f"Count of images in the training set: {len(train_df) - missing_train_count}")
    print(f"Count of images in the validation set: {len(val_df) - missing_val_count}")
    print(f"Count of images in the test set: {len(test_df) - missing_test_count}")
    print(f"Count of missing images in the training set: {missing_train_count}")
    print(f"Count of missing images in the validation set: {missing_val_count}")
    print(f"Count of missing images in the test set: {missing_test_count}")

if __name__ == "__main__":
    # Replace 'your_caption_file.csv' with the name of your caption CSV file
    caption_csv_file = '/Users/nirajanpaudel17/Downloads/stanford_cultural_nepalis.csv'

    # Replace 'your_image_folder' with the path to your image folder
    image_folder_path = '/Users/nirajanpaudel17/Downloads/stanford_images'

    # Replace 'output_folder' with the desired output folder path
    output_folder_path = '/Users/nirajanpaudel17/Desktop/dataset-captioning'

    split_images_and_captions(caption_csv_file, image_folder_path, output_folder_path)
