# import json

# with open('data.json') as f:
#     data = json.load(f)

# print(data)


import json

data = {
    'videos': 356
}
m = open("data.json")

d = json.load(m)
print(type(d["videos"]))

