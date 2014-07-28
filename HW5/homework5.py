### Homework 5 ###

### challenge 1 ###

import arcpy
from arcpy import env
env.workspace = U:\Shared\GIS\StuData\emwill9905\Python\Data\Exercise06
feature_list = arcpy.ListFeatureClasses()
for feature in feature_list
    desc = arcpy.Describe(feature)
    
print "{} is a {1} feature".format(desc.baseline, desc.ShapeType)


### challenge 2 ###

import arcpy
from arcpy import env
env.workspace = "U:\Shared\GIS\StuData\emwill9905\Python\Data\Exercise06"
fc_list = arcpy.ListFeatureClasses()
arcpy.CreateFile GDB_management("C:/Data", "new.gdb")
for fc in fc_list:
desc = arcpy.Describe(fc)
if desc.shapeType == "Polygon":
arcpy.Copy_management (fc, "C:/Data/new.gdb/" + fc)
