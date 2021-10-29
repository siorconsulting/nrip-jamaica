import arcpy
from arcpy import env
from arcpy.sa import *
from conditional_eval import *

__all__ = ['inundation_extents']

def inundation_extents(ElevationRaster, list_thresholds=[0,5,10,15], out_raster_root_path=None, out_polygon_root_path=None):
    """ Creates a set of inundation extents based on elevation thresholds and exports them as polygons and/or rasters' 
  
    Inputs:
        ElevationRaster L raster
        list_thresholds [optional] : list
        out_raster_tool_path [optional] : str
    
    Returns:
        None
    """
    
    for i, th in enumerate(list_thresholds):

        if i==0:
            outRaster=set_null_above(inRaster,th)
            if out_raster_root_path is not None:
                outRaster.save(f"{out_raster_root_path}_below_{str(th).replace('.','p')}")
            if out_polygon_root_path is not None:
                out_polygon_features = f"{out_polygon_root_path}_below_{str(th).replace('.','p')}"
                arcpy.conversion.RasterToPolygon(outRaster, out_polygon_features)

        elif i==len(list_thresholds):
            pass
        
        else:
            low_th = th
            high_th = list_threshold[i+1]
            outRaster = set_null_between(inRatser, low_th, high_th)
            if out_raster_root_path is not None:
                outRaster.save(f"{out_raster_root_path}_from_{str(low_th).replace('.','p')}_to_{str(high_th).replace('.','p')}")
            if out_polygon_root_path is not None:
                out_polygon_features = f"{out_polygon_root_path}_from_{str(low_th).replace('.','p')}_to_{str(high_th).replace('.','p')}"
                arcpy.conversion.RasterToPolygon(outRaster, out_polygon_features)
   



