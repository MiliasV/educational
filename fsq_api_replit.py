import os
import requests, json
import csv


# API endpoint
url = 'https://api.foursquare.com/v2/venues/search'

# parameters of our query
params = dict(
client_id=os.environ['client_id'],
client_secret=os.environ['client_secret'],
v='20180323',
ll='52.372473,4.896255',
query='food',
radius='300',
limit=100
)

resp = requests.get(url=url, params=params)
data = json.loads(resp.text)

# print(data)
res = []
for v in data["response"]["venues"]:
  tmp = {}
  tmp["name"] = v['name']
  # print("Name: ",v['name'])
  tmp["cat_id"] = v['id']
  # print("Categories ID: ", v['id'])
  tmp["cat_name"] = v['categories'][0]['name']
  # print("Categories Name: ", v['categories'][0]['name'])
  tmp["latitutde"] = v['location']['lat']
  tmp["longitude"] = v['location']['lng']
  # print(v['location']['lat'], v['location']['lng'])
  print(json.dumps(res, indent=4, sort_keys=True))
  res.append(tmp)
  print("###############################################\n")

print("#########################")
print("# Results retrieved: " + str(len(data["response"]["venues"]))+ " #")
print("#########################\n")

keys = res[0].keys()
with open('result.csv', 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(res)