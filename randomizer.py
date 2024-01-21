#!/usr/bin/env python3

import random
import os
import slack

#testing = False

# instantiate Slack client
#slack_client = slack.WebClient(token=os.environ["SLACK_API_TOKEN"])

#slack params
#channel_live = ""
#channel_debug = ""

leader_names = [
"Leader 1",
"Leader 2",
"Leader 3",
"Leader 4"
]

names = [
"Person 1",
"Person 2",
"Person 3",
"Person 4",
"Person 5",
"Person 6",
"Person 7",
"Person 8",
"Person 9",
"Person 10",
"Person 11",
"Person 12",
"Person 13",
"Person 14",
"Person 15",
"Person 16",
"Person 17",
"Person 18"
]


def pick_leader():
    leader = random.choice(leader_names)
    leader_names.remove(leader)
    return "---" + leader + "---"

def pick_team(num_names):
    team = ""
    for i in range(0,num_names):
        name = random.choice(names)
        names.remove(name)
        team = team + "\n" + name
        if not names:
            break
    return team

def randomiser():
    
    num_leaders = len(leader_names)
    num_names = len(names)
    extra_names = num_names % num_leaders
    
    response = "" #"<!here> \n"
    for i in range(0, num_leaders):
        response += (pick_leader() + 
                     pick_team(num_leaders + (1 if extra_names > 0 else 0)) + 
                     "\n")
        extra_names -= 1
    
    print(response)

    #if testing:
    #    current_channel = channel_debug
    #else:
    #    current_channel = channel_live
    
    #slack_client.chat_postMessage(
    #    channel=current_channel,
    #    text=response,
    #    as_user=True
    #)

#def lambda_handler(event, context):
randomiser()
#    return("Randomiser posted successfully!")
