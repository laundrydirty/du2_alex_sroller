#import funkci z vytvoreneho modulu quadtree (a json)
import json
from quadtree import kvad_strom,bounding_box

#vstup dat ve formatu geojson
with open("input.geojson","r",encoding="utf-8") as f:
    data=json.load(f)

#extrakce pouze souradnic bodu
point_coordinates=[]
for feat in data['features']:
    coordinates=feat['geometry']['coordinates']
    point_coordinates.append(coordinates)

#extrakce pouze features
dostromu = data['features']

#spusteni funkce bounding box
xmin,xmax,ymin,ymax=bounding_box(point_coordinates)[0:4]
print(xmin,xmax,ymin,ymax)

#vytvoreni prazdnych seznamu
cluster_ID=[0]

#spusteni funkce kvad strom
kvad_strom(dostromu,xmin,xmax,ymin,ymax,cluster_ID)

#zachovani struktury geojson
gj_structure={'type': 'FeatureCollection'}
gj_structure['features']=dostromu

#vystup dat ve formatu geojson
with open("output.geojson","w",encoding="utf-8") as f:
    json.dump(gj_structure,f,indent=2,ensure_ascii=False)
