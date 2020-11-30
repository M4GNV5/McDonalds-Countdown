import json
import requests

r = requests.get("https://mcd-mobileapp-prod.azureedge.net/json/de/campaigns/appventskalender2020.json")
data = r.json()

for key in data["overlays"]:
	overlay = data["overlays"][key]
	day = key[-2 : ]
	image = overlay["items"][0]["revealImageUrl"]
	label = overlay["items"][1]["items"][1]["text"]

	print("## {}.12.2020: {}\n![]({})\n".format(day, label, image))
