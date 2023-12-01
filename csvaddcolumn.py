import pandas as pd

def add_split_columns(input_csv, output_csv):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_csv)

    # Add columns for train, test, and validation
    df['train'] = df.index.between(1, 120)
    df['test'] = df.index.between(121, 150)
    df['validation'] = ~df.index.between(1, 150)

    # Convert boolean values to 'TRUE' and 'FALSE'
    df['train'] = df['train'].map({True: 'TRUE', False: 'FALSE'})
    df['test'] = df['test'].map({True: 'TRUE', False: 'FALSE'})
    df['validation'] = df['validation'].map({True: 'TRUE', False: 'FALSE'})

    # Save the updated DataFrame to a new CSV file
    df.to_csv(output_csv, index=False)

if __name__ == "__main__":
    # Replace 'input.csv' with the path to your input CSV file
    input_csv = '/Users/nirajanpaudel17/Desktop/patan-output.csv'
import pandas as pd

def add_split_columns(input_csv, output_csv):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_csv)

    # Add columns for train, test, and validation
    df['train'] = (df.index >= 1) & (df.index <= 120)
    df['test'] = (df.index >= 121) & (df.index <= 150)
    df['validation'] = ~(df.index <= 150)

    # Convert boolean values to 'TRUE' and 'FALSE'
    df['train'] = df['train'].map({True: 'TRUE', False: 'FALSE'})
    df['test'] = df['test'].map({True: 'TRUE', False: 'FALSE'})
    df['validation'] = df['validation'].map({True: 'TRUE', False: 'FALSE'})

    # Save the updated DataFrame to a new CSV file
    df.to_csv(output_csv, index=False)

if __name__ == "__main__":
    # Replace 'input.csv' with the path to your input CSV file
    input_csv = '/Users/nirajanpaudel17/Desktop/patan-output.csv'

    # Replace 'output.csv' with the desired output CSV file name
    output_csv = '/Users/nirajanpaudel17/Desktop/patanoutput.csv'

    add_split_columns(input_csv, output_csv)

    # Replace 'output.csv' with the desired output CSV file name
    output_csv = '/Users/nirajanpaudel17/Desktop/final-caption.csv'

    add_split_columns(input_csv, output_csv)
