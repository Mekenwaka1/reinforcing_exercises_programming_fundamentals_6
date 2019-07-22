house = {"meta": {"total_count": 336, "limit": 336, "next": None, "offset": 0, "previous": None}, "objects": [{"source_url": "http://www.parl.gc.ca"}]}

print(house.keys())
print(type(house["meta"]))
print(type(house["objects"]))
print(len(house["meta"]))
print(len(house["objects"]))
print(house["objects"][0]["source_url"])