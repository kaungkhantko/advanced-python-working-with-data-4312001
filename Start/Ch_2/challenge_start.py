# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import collections
from collections import Counter
from collections import defaultdict

# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)


def extractType(q):
    if q["properties"]["type"] is None:
        return 0
    else:
        return q["properties"]["type"]


def getType(dataitem):
    type = dataitem["properties"]["felt"]
    if type is None:
        type = 0
    return str(type)


eventTypes = defaultdict(int)
for dataitem in data["features"]:
    eventTypes[extractType(dataitem)] += 1
print(eventTypes)
