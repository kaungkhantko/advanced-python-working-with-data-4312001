# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
import datetime
import pprint

# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)


def getSig(q):
    sig = q["properties"]["sig"]
    if sig is not None:
        return sig
    else:
        return 0


def getFelt(q):
    felt = q["properties"]["felt"]
    if felt is not None:
        return 0
    else:
        return felt


def simplify(q):
    coordinates = q["geometry"]["coordinates"]
    return {
        "magnitude": q["properties"]["mag"],
        "place": q["properties"]["place"],
        "felt": q["properties"]["felt"] if q["properties"]["felt"] is not None else 0,
        "date": datetime.date.fromtimestamp(int(q["properties"]["time"] / 1000)),
        "url": f"https://www.google.com/maps/search/?api=1&query={coordinates[1]},{coordinates[0]}",
    }


header = ["Magnitude", "Place", "Felt Reports", "Date", "Google Map Link"]


data["features"].sort(key=getSig, reverse=True)
results = list(map(simplify, data["features"][0:40]))

results = sorted(results, key=lambda x: x["date"], reverse=True)

rows = []
for dataitem in results:
    rows.append(
        [
            dataitem["magnitude"],
            dataitem["place"],
            dataitem["felt"],
            dataitem["date"],
            dataitem["url"],
        ]
    )

with open("Start/Ch_3/challenge.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(header)
    writer.writerows(rows)


# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD
