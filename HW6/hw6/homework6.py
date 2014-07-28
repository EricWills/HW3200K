### homework 6 (chapter 7,8) ###

###chapter 7 challenges ###

#ran into some syntax problems here while i was working through it###

### chall. 1 ###

import arcpy
from arcpy import env
env.workspace = U:/Shared/GIS/StuData/emwill9905/Python/Data/Exercise07
sql1 = " \"FEATURE\" = 'Airport'"
sql2 = " \"FEATURE\" = 'Seaplane Base'"
arcpy.Select_analysis ("airports.shp", "Results/seaports.shp", sql2)
arcpy.Buffer_analysis("Results/airports_final.shp", "Results/aiports_buffers.shp", "15000 METERS")

### C. 2 ###

import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise07"
fc = "roads.shp"
arcpy.AddField_management(fc, "FERRY", "TEXT", "", "", 20)
cursor = arcpy.da.UpdateCursor(fc, ["FEATURE", "FERRY"])
for row in cursor:
    if row[0] == "Ferry Crossing":
    row[1] = "YES"
        else:
            row[1]= "NO"
        cursor.updateRow(row)


### CHAPTER 8 ###

import arcpy
from arcpy import env
env.workspace = "U:/Shared/GIS/StuData/emwill9905/Python/Data/Exercise08"
fc = "newpoly2.shp"
arcpy.CreateFeatureclass_management("U:/Shared/GIS/StuData/emwill9905/Python/Data/Exercise08", fc, "Polygon")
cursor = arcpy.da.InsertCursor(fc, ["SHAPE@"])
array = arcpy.Array()
coordlist =[[0, 0], [0, 1000], [1000, 1000], [1000, 0]]
for x, y in coordlist:
    point = arcpy.Point(x,y)
    array.append(point)
polygon = arcpy.Polygon(array)
cursor.insertRow([polygon])


### challenge 2 ###


import arcpy
from arcpy import env
env.workspace = "U:\Shared\GIS\StuData\emwill9905\Python\Data\Exercise08"
fc = "Hawaii.shp"
newfc = "Results/Hawaii_single.shp"
arcpy.MultipartToSinglepart_management(fc, newfc)
spatialref = arcpy.Describe(newfc).spatialReference
unit = spatialref.linearUnitName
cursor = arcpy.da.SearchCursor(newfc, ["SHAPE@"])
for row in cursor:
    print ("{0} square {1}".format(row[0].area))


### Challenge 3 ###


import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise08"
fc = "Hawaii.shp"
newfc = "envelope8.shp"
desc = arcpy.Describe(fc)
spatialref = desc.spatialReference
extent = desc.extent
arcpy.CreateFeatureclass_management("U:\Shared\GIS\StuData\emwill9905\Python\Data\Exercise08"
array.append(extent.upperLeft)
array.append(extent.upperRight)
array.append(extent.lowerRight)
array.append(extent.lowerLeft)
polygon = arcpy.Polygon(array)
cursor.insertRow([polygon])
