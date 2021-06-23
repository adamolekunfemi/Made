# import os library to process files
import os
import json
import pandas as pd
import re

def transform_events_data(file_name):
    """
    This function transform events_data.
    :param file_name: A event data JSON file.
    :return : it returns a dataframe
    """
    # Your code here
    basepath = 'C:/Made.Com/'       # Declaring the base path
    storage = []
    storePD = pd.DataFrame
    # Read and create the country dataframe
    country = pd.read_csv("C:/Made.Com/countries.csv")
    #print(country)

    for file in os.listdir(basepath):
        #if file.endswith(".json") and file == file_name:
        if file == file_name:
            #print(os.path.join(basepath, file))
            #store_file = file
            with open(basepath + file) as f:
                storage = json.load(f)
                #print(storage)
                dataDF = pd.DataFrame(storage,columns=["uuid","event_type","device_type","geo_country","geo_timezone","campaign_title","campaign_type","event_id","dt_occurred","to_address"])
                dataDF["file_name"] = file_name
                #masked_address = dataDF["to_address"].to_string()
                dataDF["UID"] = re.sub(r'[^@.]', 'x', dataDF["to_address"].to_string())
                del dataDF["to_address"] # deleting the to_address after using it to anonymise


    # merging the country dataframe with the main dataframe
    return pd.DataFrame(dataDF.merge(country, on='geo_country',how='left'))
# End of loop
# testing the function with a call
#a = transform_events_data("events_data-2020-07-01.json")

#print(a)
