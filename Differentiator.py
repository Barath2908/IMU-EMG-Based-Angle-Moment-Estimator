import pandas as pd

def differentiate_data(file_path):
    # Read the Excel file
    df = pd.read_excel(file_path)

    # Iterate over each column
    for column in df.columns:
        column_data = df[column]

        # Perform numerical differentiation
        differentiated_data = column_data.diff().dropna()

        # Create a new DataFrame with differentiated data
        differentiated_df = pd.DataFrame({column: differentiated_data})

        # Save the differentiated data to a new Excel file
        differentiated_file_path = "C:/Users/ibra5/Desktop/LSTM/EMG/Codes/D01.xlsx"
        differentiated_df.to_excel(differentiated_file_path, index=False)

        print(f"Differentiated data in {column} has been saved to {differentiated_file_path}")

# Provide the path to your Excel file
file_path = "C:/Users/ibra5/Desktop/LSTM/EMG/treadmill_01_01.xlsx"

# Call the function with the file path
differentiate_data(file_path)
