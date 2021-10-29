import arcpy
from arcpy.sa import *
from conditional_eval import *

def calculate_slope(ElevationRaster):
    """Create slope raster.
    
    Inputs:
        ElevationRaster : raster
    Returns:
        outSlope : raster

    """
    outSlope = Slope(ElevationRaster)
    return outSlope


def calculate_aspect(ElevationRaster):
    """Create aspect raster.
    
    Inputs:
        ElevationRaster : raster
    Returns:
        outAspect : raster

    """
    outAspect = Aspect(ElevationRaster)
    return outAspect

def steep_areas(ElevationRaster, threshold=20, out_raster_features=None, out_polygon_features=None):
    outSlope = Slope(ElevationRaster)
    steepAreas = set_null_below(outSlope < threshold, 1)
    if out_raster_features is not None:
        steepAreas.save(out_raster_features)
    if out_polygon_features is not None:
        arcpy.conversion.RasterToPolygon(steepAreas, out_polygon_features)
    return steepAreas
    
