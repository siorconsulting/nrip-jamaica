import arcpy
from arcpy import env
from arcpy.sa import *

filename_root = ''

outFill = Fill(inSurfaceRaster, zLimit)

outFlowDirection = FlowDirection(outFill, "NORMAL")

outFlowAccumulation = FlowAccumulation(outFlowDirection)

flow_acc_threshold = 100000

outFlowAccumulationSetNull = SetNull(outFlowAccumulation < flow_acc_threshold, 1)

outFlowDirection.save()
outFlowAccumulation.save()
outFill.save()

outFillDiff = SetNull((outFill - inSurfaceRaster) < 0, 1)

outPolygons_filename(f'{filename_root}_Fill_polygons')
outPolygons = os.path.join(gdb_folder_path,gdb_name,outPolygons_filename)
arcpy.RasterToPolygon_conversion(outFillDiff, outPolygons, "NO_SIMPLIFY")



