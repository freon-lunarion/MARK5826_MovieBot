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

# location = "/Users/xxxxxxxx/Downloads/Movie_Bot/"  # replace with the full folder path where you downloaded the github repo
location = os.path.dirname(os.path.realpath(__file__)) + '/'

###################################################################
######## Slack configuration   ##########################
###################################################################
SLACK_BOT_NAME = 'Monday'

# SLACK_BOT_TOKEN='xoxb-xxxxxxxxxxxx-xxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx'
# SLACK_VERIFICATION_TOKEN='xxxxxxxxxxxxxxxxxxxxxxxx'

SLACK_BOT_TOKEN='xoxb-597388589376-638279594800-X9gLZicsWpIfGreG5rlo4w8h'
SLACK_VERIFICATION_TOKEN='3ftQdW22Cmwq2XeSkEnqfusj'

# instantiate Slack client
slack_client = SlackClient(SLACK_BOT_TOKEN) # do not change this parameter

###################################################################
######## Watson service configuration   ##########################
###################################################################

# service = ibm_watson.AssistantV1(
#     iam_apikey = 'xxxxxxxxxxxxxxxxxxxxxxxx', # replace with Password
#     url = 'https://xxxxxxxxxx.watsonplatform.net/assistant/api', # replace with Watson Assistant's Credentials - URL
#     version = '2018-09-20'
# )

# workspace_id = 'xxxxxxxxxxxxxxxxxxxxxxxx' # replace with Assistant ID

service = ibm_watson.AssistantV1(
    iam_apikey = '0B2HITIOQodvrG9zEnBsFBZQHteLtpYBEqS2KECTCMkV', # replace with Password
    url = 'https://gateway-syd.watsonplatform.net/assistant/api', # replace with Watson Assistant's Credentials - URL
    version = '2018-09-20'
)

workspace_id = 'cf182008-1628-4a21-8b4b-87b20a2de328' # replace with Assistant ID

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
