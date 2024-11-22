import pandas as pd

print("Reading in dataset and turning into a dataframe")
file_path = "MOCK_DATA_Final.csv"
garbled_df = pd.read_csv(file_path)
print("Reading in key dataset")
key_path = "Mock_Data_Key.csv"
key_df = pd.read_csv(key_path)

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

print("Checking the names and replacing if they are missing")
# Check key_df for null values before applying the fix. Make sure the key data is good and trustworthy.
garbled_df['first_name'] = merged_df.apply(
    lambda row: row['first_name_key'] if pd.notna(row['first_name_key']) and row['first_name'] != row['first_name_key'] else row['first_name'],
    axis = 1

)

garbled_df['last_name'] = merged_df.apply(
    lambda row: row['last_name_key'] if pd.notna(row['last_name_key']) and row['last_name'] != row['last_name_key'] else row['last_name'],
    axis = 1
)

garbled_df['age'] = merged_df.apply(
    lambda row: row['age_key'] if pd.notna(['age_key']) and row['age'] != row['age_key'] else row['age'],
    axis = 1
)

garbled_df['major'] = merged_df.apply(
    lambda row: row['major_key'] if pd.notna(['major_key']) and row['major'] != row['major_key'] else row['major'],
    axis = 1
)

# Drop unwanted columns
garbled_df.drop(columns = columns_to_drop, inplace = True)

cleaned_file_path = "cleaned_mock_data.csv"
garbled_df.to_csv(cleaned_file_path, index=False)
print(f"Dataset cleaned and saved to {cleaned_file_path}")
