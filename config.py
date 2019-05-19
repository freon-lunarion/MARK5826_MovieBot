###################################################################
######## Configuration files for Bot   ##########################
###################################################################

"""
    config.py 
    
    This files has all the configurations for your bot.

"""

import os
import ibm_watson
from slackclient import SlackClient

location = "/Users/xxxxxxxx/Downloads/Movie_Bot/"  # replace with the full folder path where you downloaded the github repo

###################################################################
######## Slack configuration   ##########################
###################################################################

SLACK_BOT_TOKEN='xoxb-xxxxxxxxxxxx-xxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx'
SLACK_VERIFICATION_TOKEN='xxxxxxxxxxxxxxxxxxxxxxxx'

# instantiate Slack client
slack_client = SlackClient(SLACK_BOT_TOKEN) # do not change this parameter

###################################################################
######## Watson service configuration   ##########################
###################################################################

service = ibm_watson.AssistantV1(
    iam_apikey = 'xxxxxxxxxxxxxxxxxxxxxxxx', # replace with Password
    url = 'https://xxxxxxxxxx.watsonplatform.net/assistant/api', # replace with Watson Assistant's Credentials - URL
    version = '2018-09-20'
)

workspace_id = 'xxxxxxxxxxxxxxxxxxxxxxxx' # replace with Assistant ID

###################################################################
######## Log files configuration   ##########################
###################################################################

log_commands_path = location + "logs/log_commands.py" # do not change this parameter
follow_up_path = location + "logs/followup_email.py" # do not change this parameter

###################################################################
######## Temp files configuration   ##########################
###################################################################

onetime_path = location + "nlp/nlp_solutions/onetime_run_file.py" # do not change this parameter
onetime_file = location + "nlp/nlp_solutions/onetime.txt" # do not change this parameter
