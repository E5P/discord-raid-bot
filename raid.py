import requests, os
from colorama import Fore

os.system("cls")
tokenfile = input(Fore.BLUE + "File With Tokens: " + Fore.CYAN)
inv = input(Fore.BLUE + "Server Invite Link: " + Fore.CYAN).replace("https://discord.gg/", "")
channelid = int(input(Fore.BLUE + "Channel ID: " + Fore.CYAN))
message = input(Fore.BLUE + "Message: " + Fore.CYAN)
tokens = open(tokenfile, 'r')
while True:
	for token in tokens:
		headers = {'authorization': token}
		requests.post("https://discord.com/api/v8/invites/" + inv, headers=headers)
		print(Fore.GREEN + "JOINED")
		requests.post(f"https://discord.com/api/v8/channels/{str(channelid)}/messages", data={"content": message,"nonce": str(channelid), "tts": "false"}, headers=headers)
		requests.post(f"https://discord.com/api/v8/channels/{str(channelid)}/messages", data={"content": message,"nonce": str(channelid), "tts": "false"}, headers=headers)
		requests.post(f"https://discord.com/api/v8/channels/{str(channelid)}/messages", data={"content": message,"nonce": str(channelid), "tts": "false"}, headers=headers)
		requests.post(f"https://discord.com/api/v8/channels/{str(channelid)}/messages", data={"content": message,"nonce": str(channelid), "tts": "false"}, headers=headers)
		print(Fore.GREEN + "MESSAGE SENT")