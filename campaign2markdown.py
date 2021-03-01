import json
import requests
import datetime

#r = requests.get("https://mcd-mobileapp-prod.azureedge.net/json/de/campaigns/appventskalender2020.json")
r = requests.get("https://mcd-mobileapp-prod.azureedge.net/json/de/campaigns/easter2021.json")
data = r.json()

past_days = ""
today = datetime.date.today()

print("# McDonalds Easter 2021 Countdown (Germany)\n")

entries = {}

for page in data["pages"]:
	if page["pageName"] != "calendar":
		continue

	date = page["criteria"]["startTime"][0 : 10]
	label = page["headline"]["headline"]
	image = page["items"][0]["items"][1]["overlayImageURL"]

	entry = "## {}: {}\n![]({})\n".format(date, label, image)

	dateObj = datetime.datetime.strptime(date, "%d.%m.%Y").date()
	entries[dateObj] = {
		"date": date,
		"label": label,
		"images": [],
	}

for card in data["shared"]["teaserSlider"]["cards"]:
	date = card["description"][3 : 8] + ".2021"
	date = datetime.datetime.strptime(date, "%d.%m.%Y").date()

	if date not in entries:
		raise Exception("Could not find text to {}".format(date))

	entries[date]["images"].append(card["imageURL"])

for date in entries:
	entry = entries[date]
	label = entry["label"]
	if len(entry["images"]) > 1:
		label += " + SPECIAL"

	print("## {}: {}".format(entry["date"], label))
	for url in entry["images"]:
		print("![]({})".format(url))
	print()
