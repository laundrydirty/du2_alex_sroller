import json
from quadtree import zkouska

#vstup dat
with open("input.geojson","r",encoding="utf-8") as f:
    data=json.load(f)



#vyfiltrovani souradnic bodu
point_coordinates=[]
for feat in data["features"]:
    coordinates=(feat['geometry']['coordinates'])
    point_coordinates.append(coordinates)


zkouska(point_coordinates)

print(point_coordinates)


#gj_structure={'type': 'FeatureCollection'}
#gj_structure['features']=#nejaka_promenna

#vystup dat
#with open("output.geojson","w",encoding="utf-8") as f:
#    json.dump(gj_structure,f,indent=2,ensure_ascii=False)
