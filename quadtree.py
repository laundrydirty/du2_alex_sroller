import json

#vstup dat
with open("input.geojson","r",encoding="utf-8") as f:
    data=json.load(f)



#vyfiltrovani souradnic bodu
point_coordinates=[]
for feat in data["features"]:
    coordinates=(feat['geometry']['coordinates'])
    point_coordinates.append(coordinates)
print(point_coordinates)

def zkouska(coordinates):
    pass
    #if len(coordinates)<50:
     #   for
      #  return coordinates

def bounding_box(coordinates):
    #seradit podle osy x
    coordinates.sort(key = lambda p: p[0])
    xmin=coordinates[0]
    xmax=coordinates[-1]

    #seradit podle osy y
    coordinates.sort(key=lambda p: p[1])
    ymin=coordinates[0]
    ymax=coordinates[-1]

    #stred
    xmiddle=(xmin[0]+xmax[0])/2
    ymiddle=(ymin[1] + ymax[1]) / 2

    return(xmiddle,ymiddle)

    #1. kvadrant
    if x>xmid and y>mid

    # 2. kvadrant
    if x > xmid and y < mid

    #3. kvadrant
    if x < xmid and y < mid

    #4.kvadrant
    if x < xmid and y > mid





bounding_box(point_coordinates)







#seradit
#najit minima a maxima
#vytvorit bounding box

#zacit delit na ctvrtiny, dokud vsude neni mene nez 50 bodu
#zapsat cluster id



