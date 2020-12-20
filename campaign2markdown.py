import json
import requests
import datetime

r = requests.get("https://mcd-mobileapp-prod.azureedge.net/json/de/campaigns/appventskalender2020.json")
data = r.json()

past_days = ""
today = datetime.date.today()

print("# McDonalds XMAS 2020 Countdown (Germany)\n")

for key in data["overlays"]:
	if not key.startswith("formConfirmationOverlay"):
		continue

	overlay = data["overlays"][key]
	day = key[-2 : ]
	image = overlay["items"][0]["revealImageUrl"]
	label = overlay["items"][1]["items"][0]["text"]

	entry = "## {}.12.2020: {}\n![]({} =x200)\n".format(day, label, image)

	if today.year == 2020 and today.month == 12 and today.day > int(day):
		past_days += entry + "\n"
	else:
		print(entry)

if past_days != "":
	print("# Past Days\n")
	print(past_days)
