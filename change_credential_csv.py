"""
Copyright (c) 2023 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

__author__ = "Hyeyoung Kim <hyeyokim@cisco.com>"
__copyright__ = "Copyright (c) 2023 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"


from catalyst import *
from env import *
import pprint
from datetime import datetime
import json
import csv
import logging

try:
    # Get the CatalystCenter api token
    token = get_token(env)

    # Read & Save the credential information from csv file
    log_list = []
    with open("credential.csv", 'r', encoding='utf-8-sig') as file:
        credential_reader = csv.DictReader(file)
        for row in credential_reader:
            dict_payload = {
                "userName" : row["userName"],
                "password": row["password"],
                "enablePassword": row["enablePassword"],
                "snmpVersion" : row["snmpVersion"],
                "snmpROCommunity" : row["snmpROCommunity"],
                "ipAddress" : [row["ipAddress"]],
                "cliTransport" : row["cliTransport"]
            }
            payload = json.dumps(dict_payload)

            #Change the credential of devices with CatalystCenter api
            response = change_device_confidential(env, token, payload)
            
            #Task response print
            task_id = response["taskId"]
            task_response = get_task(env, token, task_id)

            #Save the log in the list
            log_text = 'Time:{}, Ip:{}, Log:{}\n'.format(datetime.now(), row["ipAddress"], task_response)
            log_list.append(log_text)

    #Save the log in log file
    with open(env["log_path"], 'a') as logfile:
        logfile.write("\n".join(log_list))

except Exception as e:
    print(e)


