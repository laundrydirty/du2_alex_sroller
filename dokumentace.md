# Dělení adresních bodů (QUADTREE)

Program metodou quadtree dělí data do skupin, tak aby žádná skupina neměla více než 50 jednotek. (Teda nedělí, protože nefunguje.).
Skládá se z hlavního souboru split.py a modulu quadtree.py, odkud jsou importovány funkce quadtree.

### Popis 
Vstupem je soubor s názvem input ve formátu `GeoJSON`. Jedná se o FeatureColection bodů. 

Funkce `bounding_box` seřadí body podle velikosti a najde body s nejmenšími a největšími x a y souřadnicemi a tím pádem umožní stanovit výchozí obdelník.  

Minima a maxima jsou přenesena do funkce `kvad_strom`, kde je na jejich základě vypočítán střed čtyřuhelníku, což umožňuje dělení na čtyři kvadranty.
To do jakého kvadrantu bod patří je určovány v závislosti na poloze vůči středu. Pokud se v nějakém kvadrantu vyskytuje méně než 50 bodů, daným bodům je přiřazeno specifické Cluster ID. 
Funkce je rekurzivní a volá sama sebe znovu, dokud nejsou všechny body rozděleny do kvadrantů.


Výstupem je soubour s názvem output ve fomátu `GeoJSON`, kde každý bod má zachované hodnoty vstupního souboru a zároveň přiřazené Cluster ID. 
