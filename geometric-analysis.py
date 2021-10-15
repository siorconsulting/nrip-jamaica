import arcpy
from arcpy import env
from arcpy.sa import *


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
    """Calculates hotspots"""
    
    
def interection():
    """Intersect"""


