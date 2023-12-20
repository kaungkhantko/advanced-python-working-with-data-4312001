# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json

with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# for this challenge, we're going to summarize the earthquake data as follows:

# 1: How many quakes are there in total?
def totalQuakes(quake):
    return sum(any(quake) for quake in data["features"])

# 2: How many quakes were felt by at least 100 people?
def filterAtLeast100(quake):
    felt = quake["properties"]["felt"]
    if felt is not None and felt >= 100:
        return True
    else:
        return False


print(f"The number of quakes are: {totalQuakes(data["features"])}")
quakesAtLeast100 = list(filter(filterAtLeast100, data["features"]))
print(f"The number of quakes felt by at least 100 people are: {len(quakesAtLeast100)}")


# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
def getFelt(dataitem):
    felt = dataitem["properties"]["felt"]
    if felt is None:
        felt = 0
    return float(felt)



data["features"].sort(key=getFelt, reverse=True)
print(f"The quake most felt by people: {data["features"][0]["properties"]["title"]}")



# 4: Print the top 10 most significant events, with the significance value of each
def simplify(q):
    return {
        "PLACE": q["properties"]["place"],
        "MAGNITUDE": q["properties"]["mag"],
        "Significance": q["properties"]["sig"],
    }

def getSig(dataitem):
    sig = dataitem["properties"]["sig"]
    if sig is None:
        sig = 0
    return float(sig)

data["features"].sort(key=getSig, reverse=True)
for i in range(0, 10):
    print(simplify(data["features"][i]))
# open the data file and load the JSON

