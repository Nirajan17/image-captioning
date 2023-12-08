import pandas as pd

def shuffle_csv(input_file, output_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Shuffle the rows using the sample function
    shuffled_df = df.sample(frac=1).reset_index(drop=True)

    # Write the shuffled DataFrame to a new CSV file
    shuffled_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    # Replace 'input.csv' with the name of your input CSV file
    input_file_name = '/Users/nirajanpaudel17/Downloads/stanford_cultural_nepalis.csv'
    
    # Replace 'shuffled_output.csv' with the desired name for the shuffled output CSV file
    output_file_name = '/Users/nirajanpaudel17/Desktop/shuffled_output.csv'

    shuffle_csv(input_file_name, output_file_name)
