import xml.etree.ElementTree as ET
import json

tree = ET.parse("./xml/country_data.xml")
root = tree.getroot()

# print(root.tag, root.attrib)

for child in root:
  # print(child.tag, child.attrib)
  print("\nCountry:", child.get("name"))

  neighbors = list(child.findall("neighbor"))

  for neighbor in neighbors:
    print("Neighbor:", neighbor.get("name"), neighbor.get("direction"))

# find and display neighbors of country
for country in root.findall("country"):
  c_name = country.get("name")
  year = country.find("year").text
  rank = country.find("rank").text

  neighbors = []

  for n in country.findall("neighbor"):
    neighbors.append(n.attrib)

  print(f"\nCountry: {c_name}")

  for n in neighbors:
    print(f"Neighbor: {n['name']} ({n['direction']})")


# Using .iter() to update rank of countries
for rank in root.iter("rank"):
  new_rank = int(rank.text) + 10
  rank.text = str(new_rank)

  rank.set("updated", "yes")

  # .attrib gets all attributes in a dict
  print(rank.text, rank.attrib)
  # .items() gets all attributes in a list of tuples
  print(rank.text, rank.items())

# If the XML was inside a string instead of external file
data = """
<data>
  <country name="China">
    <neighbor name="Russia"/>
  </country>
  <country name="Japan">
    <neighbor name="South Korea"/>
  </country>
</data>
"""
tree2 = ET.fromstring(data)

for c in tree2:
  print(c.get("name"))
  # This
  print(c.find("neighbor").get("name"))

# and this does the same thing
for n in tree2.iter("neighbor"):
  print(n.get("name"))

xml_input = """
<data>
  <players>
    <player sex="male" style="complete-forward" type="machine">
      <shirtn>07</shirtn>
      <name>Christiano Ronaldo</name>
    </player>
    <player sex="male" style="flair-passing" type="magician">
      <shirtn>10</shirtn>
      <name>Leo Messi</name>
    </player>
  </players>
</data>
"""

tree3 = ET.fromstring(xml_input)
ballers = tree3.findall("players/player")

print("Player Count:", len(ballers))

for player in ballers:
  print(f"Name: {player.find('name').text}")
  print(f"Shirt Number: {player.find('shirtn').text}")
  print(f"Attributes: {player.attrib}")

# Parsing JSON
json_data = """
[
  {
    "id": "09",
    "name": "Vikram Negi",
    "occupation": "Programmer"
  },
  {
    "id": "10",
    "name": "Alison Tyler",
    "occupation": "Model"
  }
]
"""

j_info = json.loads(json_data)

for person in j_info:
  print("Name:", person["name"])
  print("Occupation:", person["occupation"])
