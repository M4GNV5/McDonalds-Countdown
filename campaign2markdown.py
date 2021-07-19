import json
import requests
import datetime

#r = requests.get("https://mcd-mobileapp-prod.azureedge.net/json/de/campaigns/appventskalender2020.json")
#r = requests.get("https://mcd-mobileapp-prod.azureedge.net/json/de/campaigns/easter2021.json")
r = requests.get("https://mcd-mobileapp-prod.azureedge.net/json/de/campaigns/sw2021.json")
data = r.json()

past_days = ""
today = datetime.date.today()

print("# McDonalds Summer Weeks 2021 (Germany)\n")

entries = {}

for page in data["pages"]:
	if page["pageName"] != "couponDay": # or page["style"]["backgroundMode"] != "light":
		continue

	date = page["criteria"]["startTime"][0 : 10]
	content = page["items"][0]
	if "reference" in content:
		content = data["shared"][content["reference"]]["items"][0]
	label = content["revealHeadline"]["headline"]
	image = content["revealImageUrl"]

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
