'''
While working on fixtures for a Django project, I found that as the file grew, 
it became time-consuming to manually re-sequence the primary keys in order to have product groups in sequence. 
To address this issue, I made a short Python script that automatically rewrites the primary keys in a JSON file 
to start at 1 and increment by 1 for each subsequent record. This tool takes in a JSON file containing records 
with a primary key field ("pk") and produces a revised version of the file with the "pk" field updated. 
The revised JSON data is also formatted to be indented and easy to read. 
This tool helps to streamline the process of organizing product groups within a fixture file and saves time by eliminating 
the need for manual re-sequencing of primary keys.

I will add more functionality as needed.
'''

import json


def format_json(json_data):
    """Formats the JSON data so it is indented and easy to read"""
    return json.dumps(json_data, indent=2)


def rewrite_pk(json_data):
    """Rewrites the pk field to start from 1 and increment by 1 for each record"""
    pk = 1
    for record in json_data:
        if "pk" in record:
            record["pk"] = pk
            pk += 1
        else:
            record["pk"] = pk
            pk += 1
    return json_data


# Prompt user for file name/location
file_name = input("Enter the file name/location: ")

# Open the file and load the JSON data
with open(file_name, "r") as f:
    data = json.load(f)

# Rewrite the pk field and format the JSON data
data = rewrite_pk(data)
formatted_data = format_json(data)

# Write the formatted JSON data to the file
with open("revised_" + file_name, "w") as f:
    f.write(formatted_data)

print("Done!")
