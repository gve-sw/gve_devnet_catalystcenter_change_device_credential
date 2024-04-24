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

import requests
from datetime import datetime
from time import sleep

def get_token(env):
	url = '{}/dna/system/api/v1/auth/token'.format(env['base_url'])

	response = requests.request("POST", url, auth=(env['username'], env['password']), verify=False)

	if(response.ok):
		return response.json()['Token']
	else:
		raise Exception("Error", '{time} | get_token() Error : {reason}'.format(time=datetime.now(), reason=response.json()))
		


def change_device_confidential(env, token, payload):
	url = '{}/dna/intent/api/v1/network-device'.format(env['base_url'])

	headers = {
		'x-auth-token': token,
		'Content-Type': 'application/json',
		'Accept': 'application/json'
	}

	response = requests.request("PUT", url, headers=headers, data=payload, verify=False)

	if(response.ok):
		return response.json()['response']
	else:
		raise Exception("Error", '{time} | change_device_confidential() Error : {reason}'.format(time=datetime.now(), reason=response.json()))

def get_task(env, token, taskId):
	url = '{}/dna/intent/api/v1/task/{}'.format(env['base_url'],taskId)

	headers = {
		'x-auth-token': token,
		'Content-Type': 'application/json',
		'Accept': 'application/json'
	}

	response = requests.request("GET", url, headers=headers, verify=False)

	if(response.ok):
		return response.json()['response']
	else:
		raise Exception("Error", '{time} | get_task() Error : {reason}'.format(time=datetime.now(), reason=response.json()))
