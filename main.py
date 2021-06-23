### Task 2
import utils
import os
import pandas as pd

basepath = 'C:/Made.Com/'      # Declaring the base path

AllFiles = []

## Getting all the filenames
with os.scandir(basepath) as entries:
    for entry in entries:
        file_name, file_extension = os.path.splitext(entry)
        if file_extension == ".json":
            AllFiles.append(entry.name)

# invoking the functions
list_of_dataframe = [utils.transform_events_data(filename) for filename in AllFiles]
# combining the dataframes together
combined_df = pd.concat(list_of_dataframe, ignore_index=True)
combined_df["file_date"] = combined_df["file_name"].str[12:22]

print(combined_df)
# Printing the total number of rows processed
print("Processed {} rows".format(combined_df.shape[0]))













