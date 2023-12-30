import json

ships = {}

with open("./unitbays.csv") as f:
    data = f.read()

data = data.split("\n")
for i in data:
    values = i.split(",")
    ship = values.pop(0)
    if ship not in ships.keys(): ships[ship] = []
    ships[ship].append(values)

rows = []
for ship in ships.keys():
    base_ship = list(ship.split("-"))[0]
    bay_names = [i[0] for i in ships[ship]]
    
    for bay in ships[ship]:
        if bay[0] not in bay_names:
            ships[ship].append([bay, "N/A"])


    ships[ship].sort(key=lambda x: x[0])
    ships[ship].sort(key=lambda x: not "turret" in x[0].lower())    
    print(ships[ship])

    row_labels = "Name,"
    row_values = f"{ship},"
    for bay in ships[ship]:
        if bay not in ships[base_ship] or base_ship == ship:
            row_labels += f"{bay[0]},"
            row_values += f"{bay[1]},"
    rows.append(row_labels)
    rows.append(row_values + '\n')

with open("output.csv", "w") as f:
    f.write("\n".join(rows))

data = json.dumps(ships)
data = data.replace("]],", "]],\n")
with open("output.json", "w")as f:
    f.write(data)
