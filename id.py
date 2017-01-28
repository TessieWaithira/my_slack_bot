import os
from slackclient import SlackClient 
import datetime as dt
SLACK_BOT_TOKEN='xoxb-133773503541-Mvu77DTvH0IRmfJPDIXa2Wro'

BOT_NAME = 'savages'

slack_client = SlackClient(SLACK_BOT_TOKEN)

def morning_greetings(dt, channel, message):
		timer = dt.datetime.now()
		if timer.hour == 06 and timer.second == 00 :
				slack_client.api_call(
			  "chat.postMessage",
			  channel="#"+channel,
			  text=message
			)


if __name__ == "__main__":
	while True:
		morning_greetings(dt, 'general', 'Morning love :heart:')

		




