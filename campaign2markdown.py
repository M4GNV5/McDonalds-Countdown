import json
import requests
import datetime

#r = requests.get("https://mcd-mobileapp-prod.azureedge.net/json/de/campaigns/appventskalender2020.json")
r = requests.get("https://mcd-mobileapp-prod.azureedge.net/json/de/campaigns/easter2021.json")
data = r.json()

past_days = ""
today = datetime.date.today()

print("# McDonalds Easter 2021 Countdown (Germany)\n")

for page in data["pages"]:
	if page["pageName"] != "calendar":
		continue

	date = page["criteria"]["startTime"][0 : 10]
	label = page["headline"]["headline"]
	image = page["items"][0]["items"][1]["overlayImageURL"]

	entry = "## {}: {}\n![]({})\n".format(date, label, image)

	date = datetime.datetime.strptime(date, "%d.%m.%Y").date()
	if today > date:
		past_days += entry + "\n"
	else:
		print(entry)

if past_days != "":
	print("# Past Days\n")
	print(past_days)
