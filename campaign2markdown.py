import json
import requests
import datetime

#r = requests.get("https://mcd-mobileapp-prod.azureedge.net/json/de/campaigns/appventskalender2020.json")
#r = requests.get("https://mcd-mobileapp-prod.azureedge.net/json/de/campaigns/easter2021.json")
#r = requests.get("https://mcd-mobileapp-prod.azureedge.net/json/de/campaigns/sw2021.json")
#r = requests.get("https://mcd-mobileapp-prod.azureedge.net/json/de/campaigns/easter2022.json")
r = requests.get("https://mcd-mobileapp-prod.azureedge.net/json/de/campaigns/summer22.json")
data = r.json()

past_days = ""
today = datetime.date.today()

print("# McDonalds Summer Taste 2022 (Germany)\n")

entries = {}

for page in data["pages"]:
	if not page["identifier"].startswith("LandingPage"):
		continue

	date = page["criteria"]["startTime"][0 : 10]
	label = page["items"][1]["headline"]
	image = page["stageMedia"]["url"]

	entry = "## {}: {}\n![]({})\n".format(date, label, image)

	dateObj = datetime.datetime.strptime(date, "%d.%m.%Y").date()
	if dateObj in entries:
		entries[dateObj]["images"].add(image)
	else:
		entries[dateObj] = {
			"date": date,
			"label": label,
			"images": set([image]),
		}

for date in entries:
	entry = entries[date]
	label = entry["label"]
	if len(entry["images"]) > 2:
		label += " + SPECIAL"

	print("## {}: {}".format(entry["date"], label))
	for url in entry["images"]:
		print("![]({})".format(url), end="")
	print()
	print()
