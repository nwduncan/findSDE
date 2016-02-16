## ArcGIS SDE Connection search
## Nathan Duncan
## -----------------------------------------------------------------------------
## Uses the given argument (the name of a feature class, dataset, table etc)
## to find an SDE connection which contains that item. Comes in handy if
## running a tool on multiple machines where users have named their SDE
## connections differently.
## If you're not running 10.3 change the path below to reflect your version.
## Import findSDE and run with findSDE.Search(arg)
## Example:
##
## from findSDE import find
## arcpy.env.workspace = find('SDE_SPATIAL.GISADMIN.Sewer_Chokes')
##
## -----------------------------------------------------------------------------

import arcpy, getpass, os
from os import listdir
from os.path import isfile, join

def find(test_file):
    user = getpass.getuser()
    path = join("C:\Users",user,"AppData\Roaming\ESRI\Desktop10.3\ArcCatalog")
    files = sorted([ f for f in listdir(path) if isfile(join(path,f)) ])
    for f in files:
        SDE = join(path, f)
        testLink = join(SDE, test_file)
        if arcpy.Exists(testLink):
            return SDE
            break
        else: pass
    return False
