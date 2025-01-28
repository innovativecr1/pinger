import json

with open('data.json') as f:
    data = json.load(f)

print(data)


# import json

# data = {
#     'name': 'Bob',
#     'age': '25',
#     'city': 'Los Angeles'
# }

# with open('data.json') as f:
#     d = json.load(f)
#     print(d)
#     print(d['name'])