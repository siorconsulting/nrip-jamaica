import os
from wbt_utils import *

wbt = wbt_setup()

__all__ = ['InundationExtents']

def InundationExtents(input_raster, output_polygons, threshold):

    output_raster = 'temp_raster_inundation_extents.tif'
    
    wbt.conditional_evaluation(i=input_raster,
                               output=output_raster,
                               statement=f"value <= {threshold}",
                               true = 1,
                               false = 'null')

    wbt.raster_to_vector_polygons(i=output_raster, output=output_polygons)

    os.remove(os.path.join(wbt.work_dir, output_raster))