# -*- coding: utf-8 -*-
"""
@author: GitHub@Oscarshu0719
"""

import re
from pymongo import MongoClient

# Database.
DB_NAME = "data"
CLIENT = MongoClient("mongodb://localhost:27017/")
DATABASE = CLIENT[DB_NAME]

OUTPUT_PATH = ".\\test_import_error.log"

pattern = re.compile(r'(.*)_(.*)_(.*)_(.*)_(.*)\.(?:.*)')

# Output of each case is included in one row, and logs are saved in columns. 
output_log = [[], []]

case_list = ["Check if type 'Amateur' is in type list if the video has no \
actress name",
             "Check if the types are in ascending order"
            ]

# Traverse each video in the database.
for collection in DATABASE.list_collection_names():
    for col in DATABASE[collection].find():
        match = pattern.match(col["_id"])

        video_no = match.group(1)
        video_name = match.group(2)
        actress_name = match.group(3).split(', ')
        video_type = match.group(4).split(', ') 
        favorite = 'Favorite' in video_type
        quality = match.group(5)

        """ Case 1
        Check if type 'Amateur' is in type list if the video has no actress 
        name. 
        """
        if '' in actress_name and 'Amateur' not in video_type:
            output_log[0].append(col["_id"])

        """ Case 2
        Check if the types are in ascending order.
        """
        if not all([video_type[i] < video_type[i + 1] for i in 
            range(len(video_type) - 1)]):
            output_log[1].append(col["_id"])

# Output log.
case_no = 1
with open(OUTPUT_PATH, 'w', encoding='utf8') as output:
    for case in output_log:
        output.write('Case {}: {}.\n'.format(case_no, case_list[case_no - 1]))
        output.write('Total: {}.\n'.format(len(case)))
        for log in case:
            output.write(log + '\n')
        output.write('\n')
        case_no += 1
