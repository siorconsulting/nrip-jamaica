import arcpy
from arcpy import env
from arcpy.sa import *

__all__ = ['zonal_statistics',
           'summarize_within',
           'calculate_proximity',
           'calculate_hotspots',
           
          ]

def zonal_statistics(in_zone_data, zone_field, in_value_raster, outRasterPath, statistics_type = 'MEAN'):
    """Calculates zonal statistics
    
    Inputs:
        in_zone_data : raster or feature layer
        zone_field : field (str)
        in_value_raster : raster
        statistics_type : str
        outRasterPath.: str
    
    Return:
        None 
    """
    
    outRaster = ZonalStatistics(in_zone_data, zone_field, in_value_raster, statistics_type = statistics_type)
    outRaster.save(outRasterPath)
    

def summarize_within(in_polygons, in_sum_features, out_feature_class, keep_all_polygons='KEEP_ALL', sum_fields='Sum'):
    """Calculates summarize within and exports to a feature class.
    
    Inputs:
        in_polygons : str
        in_sum_features : str
        out_feature_class : str
        keep_all_polygons : str ['Sum', 'Mean', 'Min', 'Max', 'Stddev']
        sum_fields : str
    
    Return:
        None
    """
  
    arcpy.SummarizeWithin_analysis(in_polygons, in_sum_features, out_feature_class, 
                                   keep_all_polygons = keep_all_polygons, 
                                   sum_fields = sum_fields, 
                                   )
    
def calculate_proximity(inSourceData, maxDistance, cellSize, outDirectionRaster):
    """Calculates proximity based on Euclidean distance
    
    Inputs:
        inSourceData : raster
        maxDistance : float
        cellSize : float
        outDirectionRaster : raster
        
    Return:
        outEucDistance : raster   
    """
    outEucDistance = EucDistance(inSourceData, maxDistance, cellSize, outDirectionRaster)
    return outEucDistance

def calculate_hotspots(): 
    """Calculates hotspots
    
    Inputs:
    
    Return: 
        
    """
    

def interection():
    """Intersect
        
    Inputs:
    
    Return: 
        
    """
    


