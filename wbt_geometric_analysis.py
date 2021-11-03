import os 
from wbt_utils import *
import geopandas as gpd

# import whitebox
# wbt = whitebox.WhiteboxTools()

wbt = wbt_setup()

__all__ = ['intersect', # NOT TESTED
           'zonal_statistics', # NOT TESTED
           'distance_from_points', # NOT TESTED
           'distance_from_lines', # NOT TESTED
           'distance_from_polygons', # NOT TESTED
           'distance_from_raster', # NOT TESTED
           'hotspots_from_points', # NOT TESTED
           'hotspots_from_lines', # NOT TESTED
           'hotspots_from_polygons', # NOT TESTED
           'hotspots_from_raster', # NOT TESTED
           'interpolate_points', # NOT TESTED 
           'SummarizeWithin',
          ]

def intersect(input_vector_file, overlay, output_vector_file):
    """
    Function to return all feature parts that occur in both input layers

    Inputs:
        input_vector_file: str <-- name of input vector(.shp) file
        overlay: str <-- name of input overlay vector(.shp) file
        output_vector_file: str <-- name of output vector(.shp) file

    Outputs:
        output_vector_file: shapefile  <-- output vector shapefile
    """
    wbt.intersect(input_vector_file, overlay, output_vector_file)

def zonal_statistics(input_raster, input_zones, output_raster, stat='mean', input_zones_is_raster=True):
    """Calculates zonal statistics based on an input raster, using raster or polygon zones. 
    
    Inputs:
        input_raster : str <-- input raster(.tif) file
        input_zones : str <-- input raster(.tif) or polygon(.shp)
        output_raster : str <-- output raster(.tif) file name
        stat [optional] : str <-- 
        input_zones_is_raster [optional] : boolean <-- 

    Exports:
        output_raster : raster <-- output raster(.tif) file

    Returns:
        None

    """

    if input_zones_is_raster:
        input_zones_raster = input_zones
    else:
        input_zones_raster = 'temp_input_raster.tif'
        wbt.vector_polygons_to_raster(input_zones, input_zones_raster)
    
    wbt.zonal_statistics(i=input_raster, features=input_zones_raster, output=output_raster, stat=stat)

    if not input_zones_is_raster:
        os.remove(os.path.join(wbt.work_dir,input_zones_raster))
    
def distance_from_points(input_points, output_raster):
    input_raster = 'temp_input_raster.tif'
    wbt.vector_points_to_raster(input_points,input_raster)
    wbt.euclidean_distance(input_raster, output_raster)
    os.remove(os.join.path(wbt.work_dir,input_raster))

def distance_from_lines(input_lines, output_raster):
    input_raster = 'temp_input_raster.tif'
    wbt.vector_points_to_raster(input_lines,input_raster)
    wbt.euclidean_distance(input_raster, output_raster)
    os.remove(os.join.path(wbt.work_dir,input_raster))

def distance_from_polygons(input_polygons, output_raster):
    input_raster = 'temp_input_raster.tif'
    wbt.vector_points_to_raster(input_polygons,input_raster)
    wbt.euclidean_distance(input_raster, output_raster)
    os.remove(os.join.path(wbt.work_dir,input_raster))

def distance_from_raster(input_points, output_raster):
    input_raster = 'temp_input_raster.tif'
    wbt.vector_points_to_raster(input_points,input_raster)
    wbt.euclidean_distance(input_raster, output_raster)
    os.remove(os.join.path(wbt.work_dir,input_raster))
    
def hotspots_from_points(input_points, output_raster, filterx=11, filtery=11, k=5):
    input_raster = 'temp_hotspots_from_points.tif'
    wbt.vector_points_to_raster(input_points, input_raster)
    wbt.k_nearest_mean_filter(input_raster, output_raster, filterx=filterx, filtery=filtery, k=k)
    os.remove(os.path.join(wbt.work_dir, input_raster))

def hotspots_from_lines(input_lines, output_raster, filterx=11, filtery=11, k=5):
    input_raster = 'temp_hotspots_from_lines.tif'
    wbt.vector_lines_to_raster(input_lines, input_raster)
    wbt.k_nearest_mean_filter(input_raster, output_raster, filterx=filterx, filtery=filtery, k=k)
    os.remove(os.path.join(wbt.work_dir, input_raster))

def hotspots_from_polygons(input_polygons, output_raster, filterx=11, filtery=11, k=5):
    input_raster = 'temp_hotspots_from_polygons.tif'
    wbt.vector_lines_to_raster(input_polygons, input_raster)
    wbt.k_nearest_mean_filter(input_raster, output_raster, filterx=filterx, filtery=filtery, k=k)
    os.remove(os.path.join(wbt.work_dir, input_raster))

def hotspots_from_raster(input_raster, output_raster, filterx=11, filtery=11, k=5):
    wbt.k_nearest_mean_filter(input_raster, output_raster, filterx=filterx, filtery=filtery, k=k)

def interpolate_points(input_points, output_raster):
    wbt.radial_basis_function_interpolation(i=input_points, output=output_raster)

def SummarizeWithin(input_vector, feature_polygons, output_polygon, field_to_summarize, aggfunc='mean'):
    input_vector = gpd.read_file(input_vector)
    feature_polygons = gpd.read_file(feature_polygons)
    input_vector_join = input_vector[field_to_summarize].join(other=feature_polygons,rsuffix='_polygon')
    input_vector_join.dissolve(by='FID_polygon', aggfunc=aggfunc)
    input_vector_join.to_file(os.path.join(wbt.work_dir, output_polygon))