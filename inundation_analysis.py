import arcpy
from arcpy import env
from arcpy.sa import *
from conditional_eval import *

__all__ = ['inundation_extents',
          ]

def inundation_extents(ElevationRaster, list_thresholds=[0,5,10,15]):
  """ XXX
  
  Inputs:
  
  Return:
  """
  for i, th in enumerate(list_thresholds):
                      
     if i==0:
        outRaster=set_null_above(inRaster,th)
        outRaster.save()
     elif i==len(list_thresholds):
        pass
     else:
        low_th = th
        high_th = list_threshold[i+1]
        set_null_between(inRatser, low_th, high_th)
        
   



