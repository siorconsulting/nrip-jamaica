import arcpy
from arcpy import env
from arcpy.sa import *

def set_null_between(inRaster, low_th, high_th):
  """ Creates constant valued raster based on two SetNull operations.
  
  Input:
      inRaster : raster
      low_th : float
      high_th : float
  
  Return:
      betweenRaster : raster
  
  """
  
  lowRaster = SetNull(inRaster > high_th, inRaster)
  betweenRaster = SetNull(lowRaster < low_th, 1)
  return betweenRaster

