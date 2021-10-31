import os 
import whitebox
wbt = whitebox.WhiteboxTools()

__all__ = ['euclidean_distance',
           'intersect',
           'zonal_statistics',
           'k_nearest_mean_filter',
           'vector_points_to_raster',
           'vector_lines_to_raster',
           'vector_polygons_to_raster',
          ]

def euclidean_distance(input_raster, output_raster):
    wbt.euclidean_distance(input_raster, output_raster)
    
def intersect(input_vector_file, overlay, output_vector_file):
    wbt.intersect(input_vector_file, overlay, output_vector_file)

def zonal_statistics(input_raster, input_features, output_raster, stat='mean', feature_as_raster=True):
    """Calculates zonal statistics based on an input raster, using raster or polygon zones. 
    
    Inputs:
        input_raster : str
        input_features : str
        output_raster : str
        stat [optional] : str
        feature_as_raster [optional] : boolean

    Exports:
        output_raster : raster

    Returns:
        None

    """

    if feature_as_raster:
        input_raster = input_features
    else:
        input_raster = 'temp_input_raster.tif'
        wbt.raster_to_vector_polygons(input_features, input_raster)
    
    wbt.zonal_statistics(i=input_raster, features=input_raster, output=output_raster, stat=stat)

    if not feature_as_raster:
        os.remove(os.path.join(wbt.work_dir,input_raster))
    
def k_nearest_mean_filter():
    wbt.k_nearest_mean_filter()
