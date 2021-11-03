import os 
from wbt_utils import * 

wbt = wbt_setup()

__all__ = ['HydrologicalRouting']

def ClippingByElevation(dem, output_clipped_dem):
    wbt.conditional_evaluation(i=dem, 
                                output=output_clipped_dem, 
                                statement="value > 0", 
                                true=dem, 
                                false="null")

def HydrologicalRouting(dem, output_prefix, facc_threshold=1000, remove_temp_outputs=True):


    """Hydrolgical analysis routine. 
    
    Inputs:
        dem : str <-- path to raster(.tif) file
        output_prefix : str <-- site specific name appended to each output file name
        facc_threshold : int or float <-- flow accummulation threshold value
        remove_temp_ouputs : 

    Exports:
        fill raster [temp] : 
        flow direction raster [temp] : 
        flow accumulation raster [temp] :
        flow accumulation setnull raster [temp] : 
        flow accumulation setnull lines: 
        basins raster [temp]: 
        basins polygon :
        fill depth raster :
        fill extent raster [temp] : 
        fill extent polygons :  
    
    Returns:
        None 
    
    """

    out_fill = f"{output_prefix}_fill.tif"
    out_fdir = f"{output_prefix}_fdir.tif"
    out_facc = f"{output_prefix}_facc.tif"
    out_facc_setnull = f"{output_prefix}_facc_setnull_{facc_threshold}.tif"
    out_facc_setnull_lines = f"{output_prefix}_facc_setnull_polygon_{facc_threshold}.shp"
    out_basins = f"{output_prefix}_basins.tif"
    out_basins_polygon = f"{output_prefix}_basins_polygon.shp"
    out_calculator = f"{output_prefix}_fill_depth.tif"
    out_conditional = f"{output_prefix}_fill_extent.tif"
    out_conditional_polygon = f"{output_prefix}_fill_extent_polygon.shp"

    wbt.fill_depressions_planchon_and_darboux(dem, out_fill)
    wbt.d8_pointer(out_fill, out_fdir, esri_pntr=True)
    wbt.d8_flow_accumulation(out_fdir, out_facc, pntr=True, esri_pntr=True)
    wbt.conditional_evaluation(i=out_facc, output=out_facc_setnull, statement=f"value >= {facc_threshold}", true=1, false='null') 
    wbt.raster_to_vector_lines(i=out_facc_setnull, output=out_facc_setnull_lines)
    wbt.basins(out_fdir, out_basins, esri_pntr=True)
    wbt.raster_to_vector_polygons(i=out_basins, output=out_basins_polygon)

    wbt.raster_calculator(output=out_calculator, statement=f"'{out_fill}'-'{dem}'")
    wbt.conditional_evaluation(i=out_calculator, output=out_conditional, statement="value>0", true=1, false="null")
    wbt.raster_to_vector_polygons(i=out_conditional, output=out_conditional_polygon)

    if remove_temp_outputs:
        os.remove(os.path.join(wbt.work_dir,out_fill))
        os.remove(os.path.join(wbt.work_dir,out_fdir))
        os.remove(os.path.join(wbt.work_dir,out_facc))
        os.remove(os.path.join(wbt.work_dir,out_facc_setnull))
        os.remove(os.path.join(wbt.work_dir,out_basins))
        os.remove(os.path.join(wbt.work_dir,out_conditional))




