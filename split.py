import json

#vstup dat
with open("input.geojson","r",encoding="utf-8") as f:
    data=json.load(f)


#gj_structure={'type': 'FeatureCollection'}
#gj_structure['features']=filtered_points

#vyfiltrovani seznamu obsahujici id a souradnice bodu
filtered_points=[]
for feat in data["features"]:
    coordinates=(feat['geometry']['coordinates'])
    id=(feat['properties']['@id'])
    filtered_points.append([id,coordinates])


print(data)
print(filtered_points)
#vystup dat
#with open("output.geojson","w",encoding="utf-8") as f:
#    json.dump(,indent=2,ensure_ascii=False)