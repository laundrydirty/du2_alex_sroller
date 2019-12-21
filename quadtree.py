import json

#vstup dat
with open("input.geojson","r",encoding="utf-8") as f:
    data=json.load(f)




#vyfiltrovani souradnic bodu
point_coordinates=[]
for feat in data['features']:
    coordinates=(feat['geometry']['coordinates'])
    features=data['features']
    point_coordinates.append(coordinates)
print(point_coordinates)
print(features)

def bounding_box(coordinates):
    #seradit podle osy x
    coordinates.sort(key = lambda p: p[0])
    xminimum=coordinates[0]
    xmaximum=coordinates[-1]

    #seradit podle osy y
    coordinates.sort(key=lambda p: p[1])
    yminimum=coordinates[0]
    ymaximum=coordinates[-1]

    return (xminimum,xmaximum,yminimum,ymaximum)



def quadtree(points,xmin,xmax,ymin,ymax):
    #stredy
    xmid = (xmin + xmax) / 2
    ymid = (ymin + ymax) / 2

    if len(points)<50:
        cluster_ID = cluster_number[0]
        for index in points:
            index['properties']['cluster_ID']=cluster_ID
        cluster_temporary=cluster_counter.pop()
        cluster_umber.append(cluster_temporary+1)
        return(features)
    else:
        for feat in points:
            point=feat(['geometry']['coordinates'])
        #1. kvadrant
            if point[0] >= xmid and point[1] >=ymid:
                K1.append(point)
        # 2. kvadrant
            elif point[0] > xmid and point[1] <= ymid:
                K2.append(point)
        #3. kvadrant
            elif point[0] <= xmid and point[1] < ymid:
                K3.append(point)
        #4. kvadrant
            elif point[0] < xmid and point[1] >= ymid:
                K4.append(point)

    #rekurze na jednotlive kvadranty
    quadtree(K1,xmid,xmax,ymid,ymax)
    quadtree(K2,xmin,xmid,ymid,ymax)
    quadtree(K3,xmin,xmid,ymin,ymid)
    quadtree(K4,xmid,xmax,ymin,ymid)



b_box=bounding_box(point_coordinates)

print(b_box)
print((b_box[2][0]),(b_box[1][0]),(b_box[2][1]),(b_box[3][1]))
K1 = []
K2 = []
K3 = []
K4 = []
quadtree(features,(b_box[0][0]),(b_box[1][0]),(b_box[2][1]),(b_box[3][1]))






#seradit
#najit minima a maxima
#vytvorit bounding box

#zacit delit na ctvrtiny, dokud vsude neni mene nez 50 bodu
#zapsat cluster id



