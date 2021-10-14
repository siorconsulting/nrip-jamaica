import arcpy
from arcpy import env
from arcpy.sa import *


def calculate_proximity():
    """Calculates proximity based on Euclidean distance"""
    outEucDistance = EucDistance(inSourceData, maxDistance, cellSize, outDirectionRaster)
    return outEucDistance

def calculate_hotspots(): 
    """Calculates hotspots"""
    
    
def interection():
    """Intersect"""


