#nalezeni minim a maxim vstupnich dat
def bounding_box(coordinates):
    #serazeni podle osy x
    coordinates.sort(key = lambda p: p[0])
    xminimum=coordinates[0][0]
    xmaximum=coordinates[-1][0]

    #serazeni podle osy y
    coordinates.sort(key=lambda p: p[1])
    yminimum=coordinates[0][1]
    ymaximum=coordinates[-1][0]

    return (xminimum,xmaximum,yminimum,ymaximum)


#funkce quadtree
def kvad_strom(points,xmin,xmax,ymin,ymax,cluster_ID):
    #nalezeni stredu podle kterych bude prostor dale delen
    xmid = (xmin + xmax) / 2
    ymid = (ymin + ymax) / 2

    #stop podminka: pokud je v nekterem ctyruhelniku bodu mene nez 50, bude jim prirazeno clusterID
    if len(points)<50:
        cluster_ID[0] = cluster_ID[0] + 1
        for i in points:
            i['properties']['cluster_ID']=cluster_ID[0]
        return(points)

    #vytvoreni prazdnych seznamu pro jednotlive kvadranty
    K1 = []
    K2 = []
    K3 = []
    K4 = []

    for pomocnefungujeto in points:
    #rozhodovani do jakeho kvadrantu body spadaji a zapis do odpoviadjicicho seznamu

        point=pomocnefungujeto['geometry']['coordinates']

        #1. kvadrant
        if point[0] >= xmid and point[1] >= ymid:
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
    kvad_strom(K1,xmid,xmax,ymid,ymax,cluster_ID)
    kvad_strom(K2,xmin,xmid,ymid,ymax,cluster_ID)
    kvad_strom(K3,xmin,xmid,ymin,ymid,cluster_ID)
    kvad_strom(K4,xmid,xmax,ymin,ymid,cluster_ID)








