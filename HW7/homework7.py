### Homework 7 ###

###Chapter 10###

import arcpy
from arcpy import env
env.workspace = "U:/Shared/GIS/StuData/emwill9905/Python/Data/Exercise10/Austin_TX.mxd"
mxd = arcpy.mapping.MapDocument("U:/Shared/GIS/StuData/emwill9905/Python/Data/Exercise10/Austin_TX.mxd")
df = arcpy.mapping.ListDataFrames(mxd, "Parks")[0]
lyr = arcpy.mapping.ListLayers(mxd, "parks", df)[0]
dflist = arcpy.mapping.ListDataFrames(mxd)
for dframe in dflist:
    if dframe.name <> "Parks":
        arcpy.mapping.AddLayer(dframe, lyr)
    mxd.save()
