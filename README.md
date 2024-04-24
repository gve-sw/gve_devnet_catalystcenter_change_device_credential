# gve_devnet_catalystcenter_change_device_credential
The script gathers devices' new credential information from csv file and changes the existing devices' credential information in Catalyst Center into new one by using Catalyst Center api.


## Contacts
* Hye young Kim

## Solution Components
* Catalyst Center


## Prerequisites
**Catalyst Center Credentials**: In order to use the Catalyst Center APIs, you need to make note of the IP address, username, and password of your instance of Catalyst Center. Note these values to add to the credentials file during the installation phase.

## Installation/Configuration
1. Clone this repository with `git clone [repository name]`. To find the repository name, click the green `Code` button above the repository files. Then, the dropdown menu will show the https domain name. Click the copy button to the right of the domain name to get the value to replace [repository name] placeholder.

2. Add the IP address, username, and password that you collected in the Prerequisites section to the credentials file 'env.py'.
```
    "base_url": "", #catalystcenter ip adress
    "username": "", #catalystcenter username
    "password": "", #catalystcenter password
    "version": "",  #catalystcenter version
    "log_path" : "./logs/log.txt" #Log file path
```

3. Set up a Python virtual environment. Make sure Python 3 is installed in your environment, and if not, you may download Python [here](https://www.python.org/downloads/). Once Python 3 is installed in your environment, you can activate the virtual environment with the instructions found [here](https://docs.python.org/3/tutorial/venv.html).

4. Install the requirements with `pip3 install -r requirements.txt`


## Usage
1. Add the credential information of the devices (IP address, username, password, enablePassword, snmpVersion, snmpROCommunity, cliTransport) in credential.csv file.

2. To run the code, use the command:
```
$ python3 change_credential_csv.py
```

# Screenshots
![/IMAGES/screenshot_credentialcsvfile.png](/IMAGES/screenshot_credentialcsvfile.png)

![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.