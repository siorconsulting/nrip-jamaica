import os
from wbt_utils import *

__all__ = ['SteepAreas',
           'GeomorphologicalFluvialFloodHazardAreas', # not tested
           ]

def GeomorphologicalFluvialFloodHazardAreas(working_dir):
    wbt = wbt_setup(working_dir=working_dir)
    wbt.fill_depressions_planchon_and_darboux(dem, out_fill)
    wbt.d8_pointer(out_fill, out_fdir, esri_pntr=True)
    wbt.d8_flow_accumulation(out_fdir, out_facc, pntr=True, esri_pntr=True)
    wbt.conditional_evaluation(i=out_facc, output=out_facc_setnull, statement=f"value >= {facc_threshold}", true=1, false='null')
    wbt.buffer_raster(out_facc_setnull, out_facc_setnull_buffer, size=buffer_distance)
    wbt.raster_to_vector_polygons(out_facc_setnull_buffer, out_facc_setnull_buffer_polygon)

def SteepAreas(dem, threshold, slope_output, raster_output, polygon_output, working_dir='', delete_temp_outputs=True):
    """Create mask of areas with slope equal or higher than a threshold, and export as raster and vector files.
    
    Inputs:
        dem : raster
        threshold : float
        slope_output : str
        raster_output : str
        polygon_output : str
        working_dir [optional] : str
        delete_temp_outputs [optional] : boolean

    Returns:
        None 
        
    """
    wbt = wbt_setup(working_dir=working_dir)

    wbt.slope(dem, slope_output)
    wbt.conditional_evaluation(i=slope_output,
                               output=raster_output,
                               statement=f'value > {threshold}',
                               true=1,
                               false='null',
                               )


    # temp_polygon_output = 'temp_polygon_output.shp'
    wbt.raster_to_vector_polygons(i=raster_output, output=polygon_output)

    # wbt.dissolve(temp_polygon_output, polygon_output)         
    
    if delete_temp_outputs:
        # os.remove(os.path.join(working_dir,temp_polygon_output))
        os.remove(os.path.join(working_dir,slope_output))