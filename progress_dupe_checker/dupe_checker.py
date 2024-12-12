import pandas as pd

ms_file_path = 'ms_progess_report.csv'
hs_file_path = 'hs_progess_report.csv'


ms_df = pd.read_csv(ms_file_path)
hs_df = pd.read_csv(hs_file_path)

ms_duplicates = ms_df[ms_df.duplicated(keep = 'first')]
hs_duplicates = hs_df[hs_df.duplicated(keep = 'first')]

column_to_keep = ['KEY']

ms_filtered = ms_duplicates[column_to_keep]
ms_filtered['Source'] = 'MS Dupes'

hs_filtered = hs_duplicates[column_to_keep]
hs_filtered['Source'] = 'HS Dupes'

combined_df = pd.concat([ms_filtered, hs_filtered], ignore_index=True)




dupes_csv_file = 'dupes.csv'
combined_df.to_csv(dupes_csv_file, index=False)


