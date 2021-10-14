import arcpy
from arcpy import env
from arcpy.sa import *
from utils import *

# Define paths
gdb_folder_path = 'INSERT_GDB_FOLDER_PATH'
gdb_name = 'INSERT_GDB_NAME'

# Create geodatabase
create_geodatabase(gdb_folder_path, gdb_name)

# Define filename root
out_filename_root = 'DTM'

# Set flow accumulation threshold
flow_acc_threshold = 100000

def hydrological_routing(gdb_folder_path, gdb_name, out_filename_root, flow_acc_threshold=1000000):
    """ Hydrological routing routine, which generates the following:
        - Fill raster
        - Flow direction raster
        - Flow accumulation raster
        - Flow network polygons
        - Fill zones polygons
    """
    
    # Calculate fill 
    outFill = Fill(inSurfaceRaster, zLimit)

    # Calculate flow direction
    outFlowDirection = FlowDirection(outFill, "NORMAL")

    # Calculate flow acccumulation
    outFlowAccumulation = FlowAccumulation(outFlowDirection)

    # Calculate flow network (raster)
    outFlowAccumulationNetwork = SetNull(outFlowAccumulation < flow_acc_threshold, 1)

    # Save rasters
    outFill.save(gdb_folder_path, gdb_name, f'{out_filename_root}_fill')
    outFlowDirection.save(gdb_folder_path, gdb_name, f'{out_filename_root}_fdir')
    outFlowAccumulation.save(gdb_folder_path, gdb_name, f'{out_filename_root}_facc')

    # Calculate Fill - DTM Difference
    outFillDiff = SetNull((outFill - inSurfaceRaster) < 0, 1)

    # Convert Fill Difference raster to polygon and export
    outPolygons_filename(f'{filename_root}_Fill_polygons')
    outPolygons = os.path.join(gdb_folder_path,gdb_name,outPolygons_filename)
    arcpy.RasterToPolygon_conversion(outFillDiff, outPolygons, "NO_SIMPLIFY")

    # Convert flow network raster to polygon and export
    outPolygons_filename(f'{filename_root}_flow_network_polygons')
    outPolygons = os.path.join(gdb_folder_path,gdb_name,outPolygons_filename)
    arcpy.RasterToPolygon_conversion(outFlowAccumulationNetwork, outPolygons, "NO_SIMPLIFY")
