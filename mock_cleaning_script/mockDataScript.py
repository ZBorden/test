import pandas as pd

print("Reading in dataset and turning into a dataframe")
file_path = "MOCK_DATA_Final.csv"
garbled_df = pd.read_csv(file_path)
print("Reading in key dataset")
key_path = "Mock_Data_Key.csv"
key_df = pd.read_csv(key_path)

# ------------- Start of Functions ---------------#
def update_column(data, key_data, column_name):
    return key_data.apply(
        lambda row: row[f"{column_name}_key"]
        if pd.notna(row[f"{column_name}_key"]) and row[column_name] != row[f"{column_name}_key"]
        else row[column_name],
        axis = 1
    )

# ------------- End of Functions -------------------#



#Define columns that need to be dropped
columns_to_drop = ['duplicate_id', 'misc_notes', 'temporary_code', 'student_notes', 'is_graduated', 'name_combined', 'archived']

print("Merge the key values onto the mock sheet")
merged_df = pd.merge(
    garbled_df,
    key_df[['student_id', 'first_name', 'last_name', 'age', 'major']],
    on = 'student_id',
    how = 'left',
    suffixes = ('', '_key')
)


print("Merged df columns:", merged_df.columns)

if key_df.isnull().values.any(): 
    print("Found Nulls in the key dataset stopping script")
    sys.exit(0)
else:
    print("No missing values on the key dataset")

garbled_df['first_name'] = update_column(garbled_df, merged_df, 'first_name')
garbled_df['last_name'] = update_column(garbled_df, merged_df, 'last_name')
garbled_df['age'] = update_column(garbled_df, merged_df, 'age')
garbled_df['major'] = update_column(garbled_df, merged_df, 'major')
# Drop unwanted columns
garbled_df.drop(columns = columns_to_drop, inplace = True)

cleaned_file_path = "cleaned_mock_data.csv"
garbled_df.to_csv(cleaned_file_path, index=False)
print(f"Dataset cleaned and saved to {cleaned_file_path}")
